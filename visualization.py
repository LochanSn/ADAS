import cv2
import numpy as np

# Load Camera Image
image = cv2.imread("sample_frame.jpg")  # Change to actual image path

# Projected pixel coordinates from Step 2 (example)
pixel_coords = np.array([
    [700, 350],  # Car
    [650, 400],  # Pedestrian
    [750, 370]   # Bike
])

# Corresponding object labels
objects = [
    {"label": "Car", "distance": 18, "speed": 3},
    {"label": "Pedestrian", "distance": 8, "speed": 1},
    {"label": "Bike", "distance": 25, "speed": 6}
]

# Function to overlay radar data on camera image
def draw_detections(image, pixel_coords, objects):
    for (x, y), obj in zip(pixel_coords, objects):
        # Draw a circle at the detected object location
        cv2.circle(image, (int(x), int(y)), 8, (0, 0, 255), -1)

        # Draw label with distance & speed
        label = f"{obj['label']} | {obj['distance']}m | {obj['speed']}m/s"
        cv2.putText(image, label, (int(x) - 50, int(y) - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    return image

# Overlay detections
output_image = draw_detections(image, pixel_coords, objects)

# Save & Show the Image
cv2.imwrite("output_frame.jpg", output_image)
cv2.imshow("Radar Overlay", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
