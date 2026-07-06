from pathlib import Path
import numpy as np
import torch
import rasterio

from src.models.physics_unet import PhysicsUNet


DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def read_band(path):
    with rasterio.open(path) as src:
        arr = src.read(1).astype(np.float32)
    return arr


def normalize_band(arr):
    arr = np.nan_to_num(arr)
    p2, p98 = np.percentile(arr, (2, 98))
    arr = np.clip(arr, p2, p98)
    arr = (arr - p2) / (p98 - p2 + 1e-8)
    return arr.astype(np.float32)


def safe_index(a, b):
    return (a - b) / (a + b + 1e-8)


def prepare_input(city_folder):
    city_folder = Path(city_folder)

    b3 = read_band(next(city_folder.glob("*SR_B3.tif")))
    b4 = read_band(next(city_folder.glob("*SR_B4.tif")))
    b5 = read_band(next(city_folder.glob("*SR_B5.tif")))
    b6 = read_band(next(city_folder.glob("*SR_B6.tif")))
    b7 = read_band(next(city_folder.glob("*SR_B7.tif")))
    thermal = read_band(next(city_folder.glob("*ST_B10.tif")))

    thermal = normalize_band(thermal)

    ndvi = safe_index(b5, b4)
    ndwi = safe_index(b3, b5)
    ndbi = safe_index(b6, b5)
    swir2 = normalize_band(b7)

    ndvi = normalize_band(ndvi)
    ndwi = normalize_band(ndwi)
    ndbi = normalize_band(ndbi)

    stacked = np.stack(
        [thermal, ndvi, ndwi, ndbi, swir2],
        axis=-1
    )

    h, w, _ = stacked.shape

    h_crop = (h // 128) * 128
    w_crop = (w // 128) * 128

    stacked = stacked[:h_crop, :w_crop, :]

    return stacked


def load_model(checkpoint_path):
    model = PhysicsUNet(in_channels=5, out_channels=3).to(DEVICE)

    checkpoint = torch.load(
        checkpoint_path,
        map_location=DEVICE
    )

    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()

    return model


@torch.no_grad()
def predict_full_image(model, input_tensor, patch_size=128):
    h, w, c = input_tensor.shape

    output = np.zeros((h, w, 3), dtype=np.float32)

    for y in range(0, h, patch_size):
        for x in range(0, w, patch_size):
            patch = input_tensor[y:y + patch_size, x:x + patch_size, :]

            patch_tensor = torch.from_numpy(patch).permute(2, 0, 1)
            patch_tensor = patch_tensor.unsqueeze(0).to(DEVICE)

            pred = model(patch_tensor)

            pred_np = pred.squeeze(0).cpu().permute(1, 2, 0).numpy()
            output[y:y + patch_size, x:x + patch_size, :] = pred_np

    output = np.clip(output, 0, 1)
    return output


def run_final_pipeline(city_folder, checkpoint_path):
    model = load_model(checkpoint_path)

    input_tensor = prepare_input(city_folder)

    rgb_output = predict_full_image(
        model,
        input_tensor,
        patch_size=128
    )

    return input_tensor, rgb_output