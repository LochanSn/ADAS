import numpy as np

# Example detected objects from radar-camera fusion
detections = [
    {"label": "Car", "distance": 18, "speed": 3, "confidence": 0.9},
    {"label": "Pedestrian", "distance": 8, "speed": 1, "confidence": 0.4},  # Low confidence (False Positive)
    {"label": "Bike", "distance": 25, "speed": 6, "confidence": 0.95},
    {"label": "Unknown", "distance": 5, "speed": 0, "confidence": 0.2}  # Likely a false detection
]

# Define a minimum confidence threshold (adjust as needed)
CONFIDENCE_THRESHOLD = 0.6

# Function to filter detections
def filter_detections(detections, threshold):
    filtered_detections = [d for d in detections if d["confidence"] >= threshold]
    return filtered_detections

# Apply filtering
filtered_detections = filter_detections(detections, CONFIDENCE_THRESHOLD)

print("✅ Filtered Detections (High Confidence Only):")
for d in filtered_detections:
    print(f"{d['label']} | Distance: {d['distance']}m | Speed: {d['speed']}m/s | Confidence: {d['confidence']}")
