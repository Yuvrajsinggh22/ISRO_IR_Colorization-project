import sys
from pathlib import Path
import time
from io import BytesIO
import matplotlib.pyplot as plt

import streamlit as st
import numpy as np
from PIL import Image

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from src.inference.final_pipeline import run_final_pipeline


st.set_page_config(
    page_title="IR Satellite Image Colorization",
    page_icon="🛰️",
    layout="wide"
)

CHECKPOINT_PATH = ROOT_DIR / "outputs" / "checkpoints" / "best_physics_unet_hybrid.pth"
RAW_DIR = ROOT_DIR / "data" / "raw"


def numpy_to_png_bytes(img_array):
    img_array = np.clip(img_array, 0, 1)
    img_uint8 = (img_array * 255).astype(np.uint8)

    image = Image.fromarray(img_uint8)
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()


st.title("🛰️ Infrared Satellite Image Colorization")
st.markdown(
    """
    **Physics-Guided U-Net with Hybrid Loss**  
    Converts Landsat thermal/infrared data into realistic RGB images using
    thermal and spectral physics priors.
    """
)

st.sidebar.title("ISRO Hackathon")
st.sidebar.markdown("---")

st.sidebar.header("Select Raw Image")

raw_tif_files = sorted(list(RAW_DIR.rglob("*.tif")))

if len(raw_tif_files) == 0:
    st.error("No .tif files found inside data/raw.")
    st.stop()

selected_tif = st.sidebar.selectbox(
    "Choose raw .tif band file",
    raw_tif_files,
    format_func=lambda p: f"{p.parent.name} / {p.name}"
)

city_folder = selected_tif.parent
selected_scene = selected_tif.parent.name

st.sidebar.info(f"Selected scene: {selected_scene}")
st.sidebar.caption(f"Selected file: {selected_tif.name}")

st.sidebar.markdown("---")
st.sidebar.header("Input Features")
st.sidebar.write("• Thermal")
st.sidebar.write("• NDVI")
st.sidebar.write("• NDWI")
st.sidebar.write("• NDBI")
st.sidebar.write("• SWIR2")

st.sidebar.markdown("---")
st.sidebar.header("Final Model Metrics")
st.sidebar.metric("PSNR", "27.79 dB")
st.sidebar.metric("SSIM", "0.9465")
st.sidebar.metric("Inference", "~40 ms/tile")
st.sidebar.metric("FPS", "~25")


st.subheader("Selected Scene")
st.code(str(city_folder))

run_btn = st.button("🚀 Run Colorization", use_container_width=True)

if run_btn:
    if not city_folder.exists():
        st.error("Selected scene folder not found.")
        st.stop()

    if not CHECKPOINT_PATH.exists():
        st.error("Checkpoint not found.")
        st.stop()

    with st.spinner("Running final colorization pipeline..."):
        start = time.time()

        input_tensor, rgb_output = run_final_pipeline(
            city_folder=city_folder,
            checkpoint_path=CHECKPOINT_PATH
        )

        end = time.time()

    elapsed = end - start

    st.success(f"Prediction completed in {elapsed:.2f} seconds")

    thermal = input_tensor[:, :, 0]
    ndvi = input_tensor[:, :, 1]
    ndwi = input_tensor[:, :, 2]
    ndbi = input_tensor[:, :, 3]
    swir2 = input_tensor[:, :, 4]

    st.markdown("## Output Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Input Thermal")
        st.image(
            thermal,
            clamp=True,
            use_container_width=True
        )

    with col2:
        st.subheader("Predicted RGB")
        st.image(
            rgb_output,
            clamp=True,
            use_container_width=True
        )

    st.markdown("## Physics Prior Maps")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.image(
     plt.cm.Greens(ndvi),
     caption="NDVI - Vegetation",
     use_container_width=True
)
    
    with c2:
        st.image(
     plt.cm.Blues(ndwi),
     caption="NDWI - Water",
     use_container_width=True
)

    with c3:
        st.image(
    plt.cm.copper(ndbi),
    caption="NDBI - Built-up",
    use_container_width=True
)

    with c4:
        st.image(
    plt.cm.inferno(swir2),
    caption="SWIR2",
    use_container_width=True
)

    st.markdown("## Final Evaluation Summary")

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric("PSNR", "27.79 dB")

    with m2:
        st.metric("SSIM", "0.9465")

    with m3:
        st.metric("Runtime", f"{elapsed:.2f} sec")

    with m4:
        st.metric("Model", "Physics U-Net")

    png_bytes = numpy_to_png_bytes(rgb_output)

    st.download_button(
        label="⬇️ Download Predicted RGB PNG",
        data=png_bytes,
        file_name=f"{selected_scene}_colorized_rgb.png",
        mime="image/png",
        use_container_width=True
    )

else:
    st.info("Select a satellite scene from the sidebar and click Run Colorization.")