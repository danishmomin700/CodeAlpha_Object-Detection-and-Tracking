import cv2
from ultralytics import YOLO

model = YOLO("yolo26n.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam nahi mila!")
    exit()

while True:
    success, frame = cap.read()

    if not success:
        break

    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        conf=0.4,
        verbose=False
    )

    output = results[0].plot()

    cv2.imshow("Object Detection and Tracking", output)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()