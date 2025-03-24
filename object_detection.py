import torch
from ultralytics import YOLO  # Install using `pip install ultralytics`

# ✅ Enable GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"

# ✅ Load YOLOv8 Model (Replace with your custom-trained model if available)
model = YOLO("yolov8n.pt").to(device)  # 'yolov8n.pt' is the smallest & fastest YOLOv8 model

# ✅ Perform Object Detection on Image
image_path = "sample_frame.jpg"
results = model.predict(source=image_path, conf=0.25, device=device, imgsz=320)

# ✅ Process Detections
detected_objects = []

for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()  # Bounding box coordinates
        class_id = int(box.cls[0])  # Get detected class index
        confidence = float(box.conf[0])  # Confidence score

        # Get class name from YOLO model
        class_name = model.names[class_id]

        # Simulate Distance & Speed (Replace with real Lidar/Radar values)
        distance = round(torch.rand(1).item() * 50, 2)  # Random distance in meters
        relative_speed = round(torch.rand(1).item() * 10, 2)  # Random speed in m/s

        detected_objects.append({
            "type": class_name,
            "distance": distance,
            "relative_speed": relative_speed,
            "confidence": confidence
        })

        # ✅ Draw Bounding Box & Label
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(image, f"{class_name} {confidence:.2f}", (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# ✅ Save Detection Results
with open("sensor_data.json", "w") as file:
    json.dump(detected_objects, file, indent=4)

print("✅ Detection results saved in `sensor_data.json`")
