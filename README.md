# CubeSat Vision-Based Localization

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
cubesat-vision-estimation/
│── data/                     # Dataset used for training and evaluation
│── models/                   # Trained YOLOv8 models
│── src/                      # Source code
│   ├── medirDistYoloCV2.py   # CubeSat detection script
│   ├── pecmcv_SBC.py         # Position estimation script
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
python>=3.8
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
Below are visualizations of the model’s performance in terms of detection accuracy and localization error:

### **Detection Performance**
![Cubesat detected in 2 scenarios](https://drive.google.com/file/d/1_5OJC3oxr_qYgtmT6hjIPgYmm_Aa5G9x/view)

### **Localization Performance**
![Cubesat localisation in many positions](https://drive.google.com/file/d/1k5oD4RdfnxMjDbPXgkOfk-HoQOSB2oL2/view?usp=sharing)

## Citation
If you use this project in your research, please cite the authors:
- [vitorshaft](https://github.com/vitorshaft)
- [igorjrd](https://github.com/igorjrd)
- [sergioh25](https://github.com/sergioh25)

## Contact
For any questions or collaborations, feel free to reach out via GitHub Issues or email:
[vdmrvitor@gmail.com](vdmrvitor@gmail.com)