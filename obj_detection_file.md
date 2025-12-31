# Real-Time Object Detection using YOLOv8 and OpenCV

## Project Description
This project performs real-time object detection using a webcam.
YOLOv8 is used for detecting objects and OpenCV is used for video capture
and displaying the detected objects.

The system captures live video from the camera, detects objects frame by
frame, and shows bounding boxes around detected objects.

## Technologies Used
- Python
- OpenCV (cv2)
- Ultralytics YOLOv8
- Webcam

## Model Used
- YOLOv8 Nano (yolov8n.pt)

## How the Project Works
1. The webcam captures live video.
2. Each video frame is passed to the YOLOv8 model.
3. The model detects objects in the frame.
4. Bounding boxes are drawn on detected objects.
5. The output is displayed in a window in real time.
6. Press 'q' to stop the program.

## Installation Steps
1. Install Python
2. Install required libraries using the following commands:

   pip install ultralytics
   pip install opencv-python

## How to Run the Project
1. Connect a webcam to your system.
2. Open the project folder in VS Code.
3. Run the Python file.
4. A window will open showing live object detection.
5. Press 'q' to exit.

## Output
- Live video stream from webcam
- Detected objects are highlighted with bounding boxes
- Real-time object detection result

## Applications
- Surveillance systems
- Security monitoring
- Smart cameras
- Real-time vision applications

## Conclusion
This project demonstrates how YOLOv8 can be used with OpenCV
for efficient and real-time object detection using a webcam.
