import numpy as np
import cv2

# Camera Intrinsic Matrix (Example Values - Replace with real calibration data)
K = np.array([[800, 0, 640],  # fx, 0, cx
              [0, 800, 360],  # 0, fy, cy
              [0, 0, 1]])      # Homogeneous coordinates

# Sample radar data: (distance, angle in degrees)
radar_data = np.array([[15, 30], [25, -15], [10, 0]])  

# Convert radar polar coordinates (distance, angle) to Cartesian (x, y)
x = radar_data[:, 0] * np.cos(np.radians(radar_data[:, 1]))  # x = d * cos(angle)
y = radar_data[:, 0] * np.sin(np.radians(radar_data[:, 1]))  # y = d * sin(angle)

# Convert to homogeneous coordinates
radar_homogeneous = np.vstack((x, y, np.ones_like(x)))

# Project radar points into camera view using intrinsic matrix
image_coords = K @ radar_homogeneous
image_coords /= image_coords[2]  # Normalize by depth

# Display transformed radar points on an empty image
image = np.zeros((720, 1280, 3), dtype=np.uint8)  # Blank image
for i in range(image_coords.shape[1]):
    cv2.circle(image, (int(image_coords[0, i]), int(image_coords[1, i])), 5, (0, 0, 255), -1)

cv2.imshow("Radar Mapped to Camera", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
