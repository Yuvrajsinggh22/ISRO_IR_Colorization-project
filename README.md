<<<<<<< HEAD
# 🌍 Physics-Guided Infrared Image Colorization & Enhancement for Satellite Object Interpretation

> **ISRO National Hackathon 2026**
> **Problem Statement:** Infrared Image Colorization and Enhancement for Improved Object Interpretation

---

## 🚀 Live Demo

**🔗 Streamlit App:**  
https://isroircolorization-qqk65qfo9g8nq9woyvaxug.streamlit.app/

## 🚀 Full Report
**🔗 Report link:**
https://drive.google.com/file/d/1rKYZuUmT-VpxwaxwkhmwF_1Cq2j02_HJ/view?usp=drive_link
## 🚀 Overview

Satellite thermal infrared imagery enables Earth observation during night-time and adverse weather conditions. However, infrared images are inherently monochromatic, low in contrast, and lack the semantic richness of visible-spectrum imagery, making human interpretation and downstream computer vision tasks significantly more difficult.

This project presents a **Physics-Guided Deep Learning Framework** that translates **single-channel thermal infrared images into realistic RGB satellite imagery** while preserving structural integrity and physical consistency.

Unlike conventional image translation methods, our framework incorporates **remote sensing physics priors** to guide the learning process, resulting in more accurate and semantically meaningful colorization.

---

# 🎯 Problem Statement

The proposed solution addresses four key challenges:

* Enhance structural details of thermal satellite imagery.
* Predict realistic RGB representations from monochrome infrared images.
* Preserve semantic consistency of land-cover regions.
* Improve interpretability for human analysts and downstream AI systems.

---

# ✨ Key Features

* 🌡 Physics-Guided U-Net Architecture
* 🛰 Landsat-9 Thermal → RGB Translation
* 🌿 NDVI-based Physical Prior Integration
* 🎨 Hybrid Loss Function
* 📈 Quantitative Evaluation (PSNR & SSIM)
* ⚡ Real-time Streamlit Visualization
* 🗺 Interactive Scene Selection
* 🔍 Error Map Visualization
* 📊 Comparative Benchmarking with Multiple Architectures

---

# 🏗 Final Architecture

```
Raw Thermal Image
        │
        ▼
Preprocessing
(Normalization + Patch Extraction)
        │
        ▼
Physics Prior Generation
        │
        ├── NDVI Prior
        ├── Edge Features
        └── Structural Guidance
        │
        ▼
Physics-Guided U-Net
        │
        ▼
Hybrid Loss Optimization
(L1 + SSIM + Physics Consistency)
        │
        ▼
Predicted RGB Image
        │
        ▼
Evaluation
(PSNR, SSIM, Visual Analysis)
        │
        ▼
Interactive Streamlit Dashboard
```

---

# 🧠 Model Development Journey

We evaluated multiple architectures before selecting the final solution.

| Model                                  | Loss Function           | Epochs | PSNR      | SSIM      | Status        |
| -------------------------------------- | ----------------------- | ------ | --------- | --------- | ------------- |
| Cross-Attention Spectral Fusion        | L1                      | 20     | 25.83     | 0.917     | Experimental  |
| Cross-Attention + Hybrid Loss          | L1 + SSIM + Physics     | 20     | 26.29     | 0.934     | Improved      |
| Physics-Guided U-Net                   | L1                      | 20     | 26.50     | 0.923     | Baseline      |
| **Physics-Guided U-Net + Hybrid Loss** | **L1 + SSIM + Physics** | **20** | **27.79** | **0.946** | ✅ Final Model |

---

# 📊 Why Physics-Guided U-Net?

The final model demonstrated:

* Highest PSNR
* Highest SSIM
* Better structural preservation
* More realistic color reconstruction
* Stable convergence
* Lower visual artifacts
* Improved semantic consistency

---

# 🧩 Hybrid Loss Function

The proposed Hybrid Loss consists of three complementary objectives:

### 1. L1 Reconstruction Loss

Ensures accurate pixel-wise RGB reconstruction.

### 2. Structural Similarity (SSIM) Loss

Preserves textures and structural details.

### 3. Physics Consistency Loss

Maintains consistency with remote sensing physics priors generated from infrared imagery.

Overall Loss:

```
Hybrid Loss =
0.6 × L1
+
0.3 × SSIM
+
0.1 × Physics Consistency
```

---

# 📂 Dataset

**Source**

* Landsat-9 Satellite Imagery

Dataset contains paired:

* Thermal Infrared Images
* RGB Images

Preprocessing includes:

* Image normalization
* Co-registration
* Patch extraction
* Physics prior generation

---

# 📦 Patch Generation

Large satellite scenes were divided into fixed-size patches for efficient deep learning training.

Pipeline:

```
Satellite Scene
      │
      ▼
256 × 256 Patches
      │
      ▼
Training Dataset
```

---

# 📈 Evaluation Metrics

The proposed framework was evaluated using:

### Image Quality Metrics

* Peak Signal-to-Noise Ratio (PSNR)
* Structural Similarity Index (SSIM)

### Qualitative Evaluation

* Ground Truth Comparison
* Error Map Visualization
* Visual Semantic Consistency

---

# 🖥 Streamlit Dashboard

The application provides an interactive interface for:

* Scene Selection
* Thermal Image Visualization
* Physics Prior Visualization
* RGB Prediction
* Ground Truth Comparison
* Error Map Display
* Performance Metrics

---

# 🛠 Technology Stack

## Deep Learning

* PyTorch

## Computer Vision

* OpenCV
* NumPy

## Remote Sensing

* Rasterio
* GDAL
* Landsat-9

## Visualization

* Matplotlib
* Streamlit

---

# 📁 Project Structure

```
ISRO_IR_Colorization/

├── app/
├── src/
├── notebooks/
├── data/
│   ├── demo/
│   └── processed/
├── outputs/
│   └── checkpoints/
├── requirements.txt
├── README.md
└── report.pdf
```

---

# 🚀 Installation

```bash
git clone https://github.com/Arvind-kumar-08/ISRO_IR_Colorization.git

cd ISRO_IR_Colorization

pip install -r requirements.txt

streamlit run app/streamlit_app.py
```

---

# 📊 Final Results

| Metric                 | Value                              |
| ---------------------- | ---------------------------------- |
| Best Model             | Physics-Guided U-Net + Hybrid Loss |
| Training Epochs        | 20                                 |
| PSNR                   | **27.79 dB**                       |
| SSIM                   | **0.946**                          |
| Average Inference Time | ~40 ms per tile                    |
| Approximate FPS        | ~25                                |

---

# 🔮 Future Work

* Transformer-based Physics Priors
* Semantic Land-Cover Constraints
* Real-Time Satellite Processing
* Multi-Spectral Fusion
* Object Detection Integration
* Large-Scale Geospatial Deployment

---

# 👨‍💻 Authors

Developed as part of the **ISRO National Hackathon 2026** to advance satellite infrared image interpretation through physics-guided deep learning.
=======
# 🌍 Physics-Guided Infrared Image Colorization & Enhancement for Satellite Object Interpretation

> **ISRO National Hackathon 2026**
> **Problem Statement:** Infrared Image Colorization and Enhancement for Improved Object Interpretation

---

## 🚀 Live Demo

**🔗 Streamlit App:**  
https://isroircolorization-qqk65qfo9g8nq9woyvaxug.streamlit.app/

## 🚀 Full Report
**🔗 Report link:**
https://drive.google.com/file/d/1rKYZuUmT-VpxwaxwkhmwF_1Cq2j02_HJ/view?usp=drive_link
## 🚀 Overview

Satellite thermal infrared imagery enables Earth observation during night-time and adverse weather conditions. However, infrared images are inherently monochromatic, low in contrast, and lack the semantic richness of visible-spectrum imagery, making human interpretation and downstream computer vision tasks significantly more difficult.

This project presents a **Physics-Guided Deep Learning Framework** that translates **single-channel thermal infrared images into realistic RGB satellite imagery** while preserving structural integrity and physical consistency.

Unlike conventional image translation methods, our framework incorporates **remote sensing physics priors** to guide the learning process, resulting in more accurate and semantically meaningful colorization.

---

# 🎯 Problem Statement

The proposed solution addresses four key challenges:

* Enhance structural details of thermal satellite imagery.
* Predict realistic RGB representations from monochrome infrared images.
* Preserve semantic consistency of land-cover regions.
* Improve interpretability for human analysts and downstream AI systems.

---

# ✨ Key Features

* 🌡 Physics-Guided U-Net Architecture
* 🛰 Landsat-9 Thermal → RGB Translation
* 🌿 NDVI-based Physical Prior Integration
* 🎨 Hybrid Loss Function
* 📈 Quantitative Evaluation (PSNR & SSIM)
* ⚡ Real-time Streamlit Visualization
* 🗺 Interactive Scene Selection
* 🔍 Error Map Visualization
* 📊 Comparative Benchmarking with Multiple Architectures

---

# 🏗 Final Architecture

```
Raw Thermal Image
        │
        ▼
Preprocessing
(Normalization + Patch Extraction)
        │
        ▼
Physics Prior Generation
        │
        ├── NDVI Prior
        ├── Edge Features
        └── Structural Guidance
        │
        ▼
Physics-Guided U-Net
        │
        ▼
Hybrid Loss Optimization
(L1 + SSIM + Physics Consistency)
        │
        ▼
Predicted RGB Image
        │
        ▼
Evaluation
(PSNR, SSIM, Visual Analysis)
        │
        ▼
Interactive Streamlit Dashboard
```

---

# 🧠 Model Development Journey

We evaluated multiple architectures before selecting the final solution.

| Model                                  | Loss Function           | Epochs | PSNR      | SSIM      | Status        |
| -------------------------------------- | ----------------------- | ------ | --------- | --------- | ------------- |
| Cross-Attention Spectral Fusion        | L1                      | 20     | 25.83     | 0.917     | Experimental  |
| Cross-Attention + Hybrid Loss          | L1 + SSIM + Physics     | 20     | 26.29     | 0.934     | Improved      |
| Physics-Guided U-Net                   | L1                      | 20     | 26.50     | 0.923     | Baseline      |
| **Physics-Guided U-Net + Hybrid Loss** | **L1 + SSIM + Physics** | **20** | **27.79** | **0.946** | ✅ Final Model |

---

# 📊 Why Physics-Guided U-Net?

The final model demonstrated:

* Highest PSNR
* Highest SSIM
* Better structural preservation
* More realistic color reconstruction
* Stable convergence
* Lower visual artifacts
* Improved semantic consistency

---

# 🧩 Hybrid Loss Function

The proposed Hybrid Loss consists of three complementary objectives:

### 1. L1 Reconstruction Loss

Ensures accurate pixel-wise RGB reconstruction.

### 2. Structural Similarity (SSIM) Loss

Preserves textures and structural details.

### 3. Physics Consistency Loss

Maintains consistency with remote sensing physics priors generated from infrared imagery.

Overall Loss:

```
Hybrid Loss =
0.6 × L1
+
0.3 × SSIM
+
0.1 × Physics Consistency
```

---

# 📂 Dataset

**Source**

* Landsat-9 Satellite Imagery

Dataset contains paired:

* Thermal Infrared Images
* RGB Images

Preprocessing includes:

* Image normalization
* Co-registration
* Patch extraction
* Physics prior generation

---

# 📦 Patch Generation

Large satellite scenes were divided into fixed-size patches for efficient deep learning training.

Pipeline:

```
Satellite Scene
      │
      ▼
256 × 256 Patches
      │
      ▼
Training Dataset
```

---

# 📈 Evaluation Metrics

The proposed framework was evaluated using:

### Image Quality Metrics

* Peak Signal-to-Noise Ratio (PSNR)
* Structural Similarity Index (SSIM)

### Qualitative Evaluation

* Ground Truth Comparison
* Error Map Visualization
* Visual Semantic Consistency

---

# 🖥 Streamlit Dashboard

The application provides an interactive interface for:

* Scene Selection
* Thermal Image Visualization
* Physics Prior Visualization
* RGB Prediction
* Ground Truth Comparison
* Error Map Display
* Performance Metrics

---

# 🛠 Technology Stack

## Deep Learning

* PyTorch

## Computer Vision

* OpenCV
* NumPy

## Remote Sensing

* Rasterio
* GDAL
* Landsat-9

## Visualization

* Matplotlib
* Streamlit

---

# 📁 Project Structure

```
ISRO_IR_Colorization/

├── app/
├── src/
├── notebooks/
├── data/
│   ├── demo/
│   └── processed/
├── outputs/
│   └── checkpoints/
├── requirements.txt
├── README.md
└── report.pdf
```

---

# 🚀 Installation

```bash
git clone https://github.com/Arvind-kumar-08/ISRO_IR_Colorization.git

cd ISRO_IR_Colorization

pip install -r requirements.txt

streamlit run app/streamlit_app.py
```

---

# 📊 Final Results

| Metric                 | Value                              |
| ---------------------- | ---------------------------------- |
| Best Model             | Physics-Guided U-Net + Hybrid Loss |
| Training Epochs        | 20                                 |
| PSNR                   | **27.79 dB**                       |
| SSIM                   | **0.946**                          |
| Average Inference Time | ~40 ms per tile                    |
| Approximate FPS        | ~25                                |

---

# 🔮 Future Work

* Transformer-based Physics Priors
* Semantic Land-Cover Constraints
* Real-Time Satellite Processing
* Multi-Spectral Fusion
* Object Detection Integration
* Large-Scale Geospatial Deployment

---

# 👨‍💻 Authors

Developed as part of the **ISRO National Hackathon 2026** to advance satellite infrared image interpretation through physics-guided deep learning.
>>>>>>> 72e42d67fa66fe26456af5369a2712ccd7fcf0ca
