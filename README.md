# CubeSat Vision-Based Localization
<div style="display: inline_block"><br>
    <img src="scripts/media/demo.gif" alt="Projeto 1"  width="40%">
    <img src="scripts/media/localization.gif" alt="Projeto 2"  width="40%">
</div>

## Overview
This repository contains the code and resources for the research project on **position estimation of CubeSats using monocular vision and YOLOv8**. The project explores computer vision techniques for detecting and localizing CubeSats in space using a single camera, leveraging deep learning for object detection and pose estimation.

## Features
- Implementation of **YOLOv8** for real-time CubeSat detection.
- Localization using a monocular camera without depth sensors.
- Camera calibration for accurate position estimation.
- Training and evaluation scripts for deep learning models.
- Experimental results and performance metrics.

## Repository Structure
```
cubesatMonoPosEstimation/
│── data/                     # Dataset used for training and evaluation
│── models/                   # Trained YOLOv8 models
│── src/                      # Source code
│   ├── detect.py             # CubeSat detection script
│   ├── main.py               # Position estimation script MP4 video file
│   ├── pecmcv_SBC.py         # Position estimation script using USB camera
│   ├── calibraCamera.py      # Camera calibration tool
│   ├── trainYolov8n.py       # YOLOv8 training pipeline
│── results/                  # Performance results and experiment logs
│── README.md                 # Project description and instructions
│── requirements.txt          # Dependencies
│── .gitignore                # Files to be ignored in Git
```

## Getting Started
### Prerequisites
To run this project, ensure you have the following dependencies installed:
```
python>=3.9
torch
ultralytics
opencv-python
numpy
matplotlib
```
You can install them using:
```
pip install -r requirements.txt
```

### Running the Detection Script
To test CubeSat detection on an image or video:
1. Go to `/scripts` and run download_media.ipynb cells, in sequence.
2. Run the following script:
```
python scripts/medirDistYoloCV2.py
```

### Training a New Model
If you wish to train YOLOv8 on a custom dataset:
1. Go to `/data` and run download_dataset.ipynb cells, in sequence.
2. Run the following script:
```
python scripts/trainYolov8n.py
```

## Results and Performance
Below are visualizations of the model’s performance in terms of detection accuracy and labelling:

### **Trainning Performance**
![Cubesat detected in 2 scenarios](/results/results.png)

### **Labelling Validation**
![Cubesat localisation in many positions](/results/val_batch2_pred.jpg)

## Citation
If you use this project in your research, please cite the authors:
- [vitorshaft](https://github.com/vitorshaft)
- [igorjrd](https://github.com/igorjrd)
- [sergioh25](https://github.com/sergioh25)

## Contact
For any questions or collaborations, feel free to reach out via GitHub Issues or email:
[vdmrvitor@gmail.com](vdmrvitor@gmail.com)