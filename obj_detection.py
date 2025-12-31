import cv2
from ultralytics import YOLO
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while True:
    video_show , frame_showing = cap.read()
    if not video_show:
        print("fail to capture a img")
        break
        qq
    res = model(frame_showing)

    read_box = res[0].plot()

    cv2.imshow("capture images", read_box)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
