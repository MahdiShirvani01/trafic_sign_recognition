# Traffic Sign Recognition using Deep Learning

A deep learning project for classifying traffic signs using various CNN architectures including custom ResNet, SimpleCNN, and pretrained models.

## Project Overview

This project implements and compares multiple deep learning models for traffic sign classification using the German Traffic Sign Recognition Benchmark (GTSRB) dataset. The system achieves high accuracy in identifying 43 different traffic sign classes.

## Features

- **Multiple Model Architectures**:
  - Custom TinyResNet
  - SimpleCNN
  - Pretrained models (MobileNetV2, DenseNet121, EfficientNetB0, ResNet34)
- **Data Augmentation** for improved generalization
- **Comprehensive Training Pipeline** with metrics tracking
- **Model Evaluation** and performance comparison
- **GPU Acceleration** support

## Project Structure
traffic-sign-recognition/
├── test.ipynb # Main training and evaluation notebook
├── requirements.txt # Python dependencies
├── report.pdf # Project documentation and results
├── models/ # Saved model weights
│ ├── tinyresnet_best.pth
│ └── simplecnn_best.pth
└── data/ # Dataset files
├── train.p
├── valid.p
└── test.p

## Dataset

The project uses the GTSRB dataset containing:
- **Training**: 34,799 images (32×32×3)
- **Validation**: 4,410 images (32×32×3)
- **Test**: 12,630 images (32×32×3)
- **Classes**: 43 different traffic sign categories

## Model Architectures

### 1. TinyResNet
- Custom lightweight ResNet implementation
- Basic residual blocks with skip connections
- Adaptive average pooling
- Achieves ~98% validation accuracy

### 2. SimpleCNN
- Three convolutional layers with max pooling
- Dropout for regularization
- Fully connected layers for classification
- Achieves ~96% validation accuracy

### 3. Pretrained Backbones
- MobileNetV2
- DenseNet121
- EfficientNetB0
- ResNet34

## Installation

1. Clone the repository:
```bash
git clone <https://github.com/MahdiShirvani01/trafic_sign_recognition>
cd traffic-sign-recognition
pip install -r requirements.txt
