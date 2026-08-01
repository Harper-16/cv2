# 20+ Computer Vision Projects using OpenCV 🚀

Welcome to this comprehensive repository featuring **20 production-ready Computer Vision (CV) projects** built using Python and OpenCV (`cv2`). This repository spans across core domains including image processing, real-time object tracking, facial analytics, advanced deep learning integrations, and interactive vision applications.

---

## 📋 Table of Contents
1. [Prerequisites & Installation](#-prerequisites--installation)
2. [Project Catalog & Directory Structure](#-project-catalog--directory-structure)
3. [Quick Start Guide](#-quick-start-guide)
4. [Tech Stack](#-tech-stack)
5. [License](#-license)

---

## 🛠️ Prerequisites & Installation

### 1. Clone the Repository
```bash
git clone https://github.com
cd YOUR_REPO_NAME
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 📂 Project Catalog & Directory Structure

Each project lives in its own dedicated directory containing its source code, assets, and localized run instructions.

```text
├── .gitignore
├── README.md
├── requirements.txt
├── 01_image_filters/
├── 02_edge_detection/
├── 03_color_spaces/
...
└── 20_onnx_deployment/
```

### 🔹 Image Processing Fundamentals
*   **`01_image_filters/`** – Custom kernel convolutions, blurring, and morphologic operations.
*   **`02_edge_detection/`** – Canny, Sobel, and Laplacian spatial edge filters.
*   **`03_color_spaces/`** – Real-time HSV/LAB thresholding for custom segmentation masks.
*   **`04_image_stitching/`** – Panorama generator utilizing SIFT/ORB keypoints and homography matching.
*   **`05_perspective_warp/`** – Automatic document scanning via corner detection and warp transformations.

### 🔹 Real-Time Tracking & Motion
*   **`06_object_tracking/`** – Benchmark comparison of CSRT, KCF, and MOSSE tracking algorithms.
*   **`07_optical_flow/`** – Lucas-Kanade dense and sparse tracking of pixel displacement vectors.
*   **`08_background_subtraction/`** – Static background subtraction for security system motion triggers.
*   **`09_contour_analysis/`** – Industrial sorting simulation via geometric shape and area profiling.
*   **`10_optical_character_recognition/`** – Text localized and extracted using OpenCV and Tesseract.

### 🔹 Face & Human Analytics
*   **`11_face_detection/`** – Haar Cascades vs. OpenCV DNN Face Detector modules.
*   **`12_facial_landmarks/`** – 68-point shape prediction for alignment and mask overlay pipelines.
*   **`13_eye_gaze_drowsiness/`** – Driver safety module calculating Eye Aspect Ratio (EAR) alerts.
*   **`14_object_detection_dnn/`** – Single Shot MultiBox Detector (SSD) using MobileNet deployment.
*   **`15_yolov8_integration/`** – Ultralytics YOLOv8 real-time inference optimized via standard CV2 loops.

### 🔹 Advanced & Interactive Applications
*   **`16_virtual_painter/`** – In-air canvas painting utilizing real-time webcam hand tracking.
*   **`17_lane_detection/`** – Advanced automotive pipeline utilizing Hough Transforms and ROI masking.
*   **`18_qr_barcode_scanner/`** – High-throughput decode system utilizing hardware-accelerated cameras.
*   **`19_camera_calibration/`** – Camera intrinsic matrix extraction via checkerboard spatial estimation.
*   **`20_onnx_deployment/`** – Custom model acceleration running directly on the `cv2.dnn` backend.

---

## ⚡ Quick Start Guide

To launch any specific application, navigate to its respective directory and execute the main python runtime module:

```bash
# Example: Launching Project 11 (Face Detection)
cd 11_face_detection
python face_detector.py
```

> 💡 **Note:** Most real-time applications will default to index `0` for the system camera. If you have multiple capture devices connected, modify the instantiation argument within `cv2.VideoCapture(index)`.

---

## 🧰 Tech Stack

*   **Language:** Python 3.10+
*   **Core CV Core:** OpenCV (`opencv-python`)
*   **Data Processing:** NumPy, SciPy
*   **Deep Learning Hub:** PyTorch, ONNX Runtime, Ultralytics YOLO
*   **GUI & Display:** Matplotlib

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
