from ultralytics import YOLO
import cv2
import os
import torch

# ✅ Check for GPU availability
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"🚀 Using device: {device}")

# ✅ Use YOLOv8 pre-trained model (without best.pt)
model = YOLO("yolov8n.pt")  # Using YOLOv8 nano model

# ✅ Set image path
image_path = r"C:\Users\lochan sn\OneDrive\Desktop\adas\sample_frame.jpg"

# ✅ Check if image exists
if not os.path.exists(image_path):
    print(f"❌ Error: Image not found at {image_path}")
    exit()

# ✅ Load image
image = cv2.imread(image_path)
if image is None:
    print("❌ Error: Image could not be loaded. Check file format.")
    exit()

# ✅ Run object detection
results = model.predict(source=image, conf=0.25, device=device, imgsz=640)

# ✅ Draw bounding boxes
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
        cls = model.names[int(box.cls)]  # Object class
        conf = box.conf[0]  # Confidence score

        # Draw bounding box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, f"{cls} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# ✅ Show the image with detections
cv2.imshow("YOLO Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
