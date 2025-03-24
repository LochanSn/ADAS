import torch
import time
import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
from ultralytics import YOLO  # YOLOv8 Model

# ✅ Check for GPU availability
import torch

# ✅ Force YOLO to use GPU if available
if torch.cuda.is_available():
    device = "cuda"
    torch.backends.cudnn.benchmark = True  # Optimize performance
    print("🚀 GPU is available! Using CUDA for faster processing.")
else:
    device = "cpu"
    print("⚠️ GPU not available. Using CPU.")

print(f"✅ Running on: {device}")

print(f"🚀 Using device: {device}")


# ✅ Use YOLOv8 pre-trained model (not best.pt)
model = YOLO("yolov8n.pt").to(device)
  # Using YOLOv8 Nano model

# ✅ Model is now loaded correctly
print("✅ YOLO model loaded successfully!")

# ✅ Example ground truth labels (Modify based on dataset)
ground_truth = ["Car", "Pedestrian", "Bike", "Truck"]

# ✅ Example detected labels (Modify based on YOLO's predictions)
predicted_labels = ["Car", "Pedestrian", "Bike", "Unknown"]

# 🔹 Convert string labels to numerical classes
label_map = {label: idx for idx, label in enumerate(["Car", "Pedestrian", "Bike", "Truck", "Unknown"])}
y_true = [label_map[label] for label in ground_truth]
y_pred = [label_map[label] for label in predicted_labels]

# ✅ Calculate Precision, Recall, and F1-score
precision = precision_score(y_true, y_pred, average='weighted', zero_division=1)
recall = recall_score(y_true, y_pred, average='weighted', zero_division=1)
f1 = f1_score(y_true, y_pred, average='weighted', zero_division=1)

print(f"✅ Precision: {precision:.2f}")
print(f"✅ Recall: {recall:.2f}")
print(f"✅ F1-Score: {f1:.2f}")

# ✅ Confusion Matrix
cm = confusion_matrix(y_true, y_pred, labels=list(label_map.values()))
print("Confusion Matrix:\n", cm)

# ✅ Measure Processing Time (Simulation)
start_time = time.time()

# Simulate ADAS pipeline execution times
time.sleep(0.02)  # Sensor fusion (20ms)
time.sleep(0.05)  # Object detection (50ms)
time.sleep(0.01)  # Decision-making (10ms)

total_time = time.time() - start_time
fps = 1 / total_time  # Frames per second

print(f"🚀 Processing Time per Frame: {total_time:.3f} seconds")
print(f"🔥 Estimated FPS: {fps:.2f}")
