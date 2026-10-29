# Object Detection and Tracking Using YOLO and OpenCV

## 📌 Project Overview

This project performs real-time object detection and tracking using a webcam or a video file. It uses a pre-trained YOLO model to detect objects and ByteTrack to track detected objects across video frames.

The system draws bounding boxes around detected objects and displays object labels, tracking IDs, and confidence scores.

## 🎯 Objectives

- Capture real-time video using a webcam.
- Detect objects using a pre-trained YOLO model.
- Process video frames and draw bounding boxes.
- Track objects using the ByteTrack algorithm.
- Display object labels, tracking IDs, and confidence scores.

## 🛠️ Technologies Used

- Python
- OpenCV
- Ultralytics YOLO
- ByteTrack
- Visual Studio Code

## ⚙️ Installation

### 1. Install Python

Install Python on your computer if it is not already installed.

### 2. Install Required Libraries

Open the terminal and run:

```bash
pip install ultralytics opencv-python
```

### 3. Download the Project

Clone this repository or download the project files from GitHub.

### 4. Run the Project

Open the project folder in VS Code and run:

```bash
python main.py
```

The pre-trained YOLO model will be downloaded automatically if it is not already available.

## 🚀 How It Works

1. Open the webcam using OpenCV.
2. Capture video frames continuously.
3. Detect objects in each frame using YOLO.
4. Track objects using ByteTrack.
5. Draw bounding boxes, object labels, tracking IDs, and confidence scores.
6. Display the processed video in real time.

## 📷 Features

- Real-time object detection.
- Person and common object recognition.
- Object tracking with unique tracking IDs.
- Bounding boxes around detected objects.
- Confidence scores for detected objects.
- Webcam and video-file input support.

## ▶️ Controls

- Press `Q` to close the video window and stop the program.

## 📁 Project Structure

```text
object-detection-and-tracking/
├── main.py
├── README.md
└── yolo26n.pt  (downloaded model file)
```

The model file may be downloaded automatically when the program runs.

## 📈 Expected Output

The application displays a live video with bounding boxes around detected objects. Each tracked object is shown with its class label, tracking ID, and confidence score.

## 🔮 Future Improvements

- Improve detection performance in low-light conditions.
- Add video recording and output saving.
- Track objects from uploaded videos.
- Improve tracking accuracy in crowded scenes.

## 👨‍💻 Author

**Name:** DANISH MOMIN

## 📄 License

This project is intended for educational and internship purposes.
