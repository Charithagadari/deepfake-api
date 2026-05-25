# DeepFake Image Detection API

A lightweight CNN-based DeepFake image classification system for distinguishing between real and AI-generated images using FastAPI and TensorFlow.

This project is based on our published research paper:

📄 Paper: https://ieeexplore.ieee.org/document/11490016

The proposed lightweight CNN model achieves:

- 91.04% classification accuracy
- 2.1 MB model size
- 40 ms inference time on Raspberry Pi 5

The model is optimized for:

- Edge AI
- Real-time inference
- Embedded systems
- Mobile deployment
- FastAPI cloud deployment

---

# Live API Deployment

### Render Deployment

🔗 https://deepfake-api-ixx8.onrender.com/docs

Users can directly test the API through Swagger UI by uploading an image and obtaining real/fake predictions.

---

# Features

- Real vs Fake image classification
- Lightweight CNN architecture
- FastAPI backend
- Docker support
- Render cloud deployment
- Swagger UI testing
- Edge-device optimized
- Real-time inference support
- Raspberry Pi deployment support

---

# Research Paper

📄 IEEE Publication:

https://ieeexplore.ieee.org/document/11490016

---

# Datasets Used

The model was trained and evaluated using the **DeepGuardDB** dataset.

📂 Original Dataset:

https://ieee-dataport.org/documents/deepguarddb-real-and-text-image-synthetic-images-dataset

The dataset contains:

- 13,000 total images
- 6,500 real images
- 6,500 AI-generated images

The AI-generated images were produced using:

- DALL-E 3
- Stable Diffusion
- GLIDE
- IMAGEN

---

# Model Performance on Different Datasets

| Dataset | Accuracy |
|---|---|
| DeepGuardDB | 91.04% |
| DALLE | 88.48% |
| GLIDE | 98.50% |
| Stable Diffusion | 86.54% |
| IMAGEN | 84.46% |

---

# Lightweight CNN Architecture

The proposed lightweight CNN architecture contains:

- 7 Convolution layers
- Batch normalization
- Max pooling
- Global Average Pooling (GAP)
- Dropout regularization
- Sigmoid binary classifier

The architecture is optimized for:

- Low latency
- Small model size
- Real-time inference
- Edge deployment

---

# Sample Dataset Structure

```bash
dataset/
│
├── real/
│   ├── real1.jpg
│   ├── real2.jpg
│   └── ...
│
└── fake/
    ├── fake1.jpg
    ├── fake2.jpg
    └── ...
```

Training labels used:

| Label | Class |
|---|---|
| 1 | real |
| 0 | fake |

---

# Tech Stack

- Python
- FastAPI
- TensorFlow / Keras
- NumPy
- Pillow
- Docker
- Render

---

# Project Structure

```bash
deepfake-api/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── Custom_model_final.h5
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Charithagadari/deepfake-api.git
```

```bash
cd deepfake-api
```

---

# Create Virtual Environment

```bash
python -m venv deepfake_env
```

### Mac/Linux

```bash
source deepfake_env/bin/activate
```

### Windows

```bash
deepfake_env\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run FastAPI Locally

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# How to Use the API

## Step 1

Run the FastAPI server locally OR use deployed Render link:

https://deepfake-api-ixx8.onrender.com/docs

---

## Step 2

Open Swagger UI.

---

## Step 3

Navigate to:

```text
POST /predict
```

---

## Step 4

Click:

```text
Try it out
```

---

## Step 5

Upload an image.

Supported formats:

- JPG
- JPEG
- PNG

---

## Step 6

Click:

```text
Execute
```

---

# Example API Response

```json
{
  "filename": "image.jpg",
  "prediction": "real",
  "confidence": "97.23%"
}
```

---

# Docker Deployment

## Build Docker Image

```bash
docker build -t deepfake-api .
```

## Run Docker Container

```bash
docker run -p 8000:8000 deepfake-api
```

Open:

```text
http://localhost:8000/docs
```

---

# Render Deployment

The project is deployed using Docker on Render.

🔗 https://deepfake-api-ixx8.onrender.com/docs

---

# Edge AI Deployment

The lightweight CNN model was successfully deployed on Raspberry Pi 5 with:

- ~40 ms inference time
- 2 MB model size

demonstrating real-time edge AI feasibility.

---

# Applications

Potential applications include:

- Social media fake content filtering
- DeepFake image detection
- Mobile AI applications
- Surveillance systems
- Digital forensics
- Journalism authenticity verification
- IoT edge vision systems

---

# Future Work

- Real-time webcam detection
- Video deepfake detection
- Explainable AI integration
- Adversarial robustness
- Mobile app deployment
- ONNX / TensorRT optimization

---

# Citation

If you use this work, please cite:

```text
Charitha Gadari et al.,
"Classification of Real and AI Generated Images using Lightweight Deep Neural Networks"
```

Publication:

https://ieeexplore.ieee.org/document/11490016

---

# Authors

- Charitha Gadari
- Bethi Pardhasaradhi
- Pathipati Srihari
- Linga Reddy Cenkeramaddi

---

# License

This project is intended for research and educational purposes.