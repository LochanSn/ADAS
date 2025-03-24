import cv2
import numpy as np

# Load Camera Image (or use a video feed)
image = cv2.imread("sample_frame.jpg")  # Replace with live feed if needed

# Example projected pixel coordinates from sensor fusion
detections = [
    {"label": "Car", "position": (700, 350), "distance": 18, "speed": 3, "risk": "⚠️ Caution"},
    {"label": "Pedestrian", "position": (650, 400), "distance": 8, "speed": 1, "risk": "🔥 Emergency"},
    {"label": "Bike", "position": (750, 370), "distance": 25, "speed": 6, "risk": "✅ Safe"}
]

# Function to overlay detections and alerts on camera image
def draw_detections(image, detections):
    for obj in detections:
        x, y = obj["position"]
        color = (0, 255, 0)  # Green for safe objects

        if "Caution" in obj["risk"]:
            color = (0, 255, 255)  # Yellow for caution
        elif "Emergency" in obj["risk"]:
            color = (0, 0, 255)  # Red for emergency braking
        
        # Draw bounding box (approximate)
        cv2.rectangle(image, (x-40, y-40), (x+40, y+40), color, 2)

        # Draw label
        label = f"{obj['label']} | {obj['distance']}m | {obj['risk']}"
        cv2.putText(image, label, (x-50, y-50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    return image

# Overlay detections
output_image = draw_detections(image, detections)

# Save & Show the Image
cv2.imwrite("adas_dashboard_output.jpg", output_image)
cv2.imshow("ADAS Dashboard", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
