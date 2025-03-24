import pandas as pd
import numpy as np

# Example sensor data (Replace with actual data loading)
camera_data = [
    {"timestamp": 1615290461.024, "frame_id": "cam_001.jpg"},
    {"timestamp": 1615290462.011, "frame_id": "cam_002.jpg"},
    {"timestamp": 1615290463.100, "frame_id": "cam_003.jpg"},
]

radar_data = [
    {"timestamp": 1615290461.030, "object_id": "car_1", "distance": 18, "speed": 3},
    {"timestamp": 1615290462.050, "object_id": "pedestrian_1", "distance": 8, "speed": 1},
    {"timestamp": 1615290463.080, "object_id": "bike_1", "distance": 25, "speed": 6},
]

# Convert lists to DataFrame for easier processing
camera_df = pd.DataFrame(camera_data)
radar_df = pd.DataFrame(radar_data)

# Function to find the closest timestamp match
def find_closest_timestamp(camera_df, radar_df):
    synced_data = []
    
    for _, radar_row in radar_df.iterrows():
        # Calculate time differences
        time_diffs = np.abs(camera_df["timestamp"] - radar_row["timestamp"])
        closest_idx = time_diffs.idxmin()  # Get closest timestamp index
        
        # Merge data
        synced_data.append({
            "camera_frame": camera_df.loc[closest_idx, "frame_id"],
            "radar_timestamp": radar_row["timestamp"],
            "object_id": radar_row["object_id"],
            "distance": radar_row["distance"],
            "speed": radar_row["speed"]
        })
    
    return pd.DataFrame(synced_data)

# Get synchronized sensor data
synced_sensor_data = find_closest_timestamp(camera_df, radar_df)

# Save to CSV or JSON for further processing
synced_sensor_data.to_csv("synced_sensor_data.csv", index=False)
print("✅ Synchronized Sensor Data Saved!")



import numpy as np
import cv2

# Example Radar point in 3D space (x, y, z in meters)
radar_points = np.array([
    [10, 2, 1],  # Example car detected by Radar
    [5, -1, 0],  # Example pedestrian
    [15, 3, 1.5] # Example bike
])

# Camera Intrinsic Parameters (from calibration)
camera_matrix = np.array([
    [1000, 0, 640],  # fx, 0, cx
    [0, 1000, 360],  # 0, fy, cy
    [0, 0, 1]        # 0, 0, 1
])

# Camera Extrinsic Parameters (Rotation + Translation)
rotation_matrix = np.array([
    [0.999, 0, 0.001], 
    [0, 1, 0],
    [-0.001, 0, 0.999]
])

translation_vector = np.array([0.1, 0.2, 1])  # Offset of Camera from Radar in meters

# Convert Radar 3D points to Camera Coordinate System
def radar_to_camera(radar_points, rotation_matrix, translation_vector):
    # Apply rotation
    rotated_points = np.dot(rotation_matrix, radar_points.T).T
    
    # Apply translation
    camera_coords = rotated_points + translation_vector
    
    return camera_coords

# Convert 3D Camera Coordinates to 2D Pixel Coordinates
def project_to_image(camera_coords, camera_matrix):
    # Convert 3D (X, Y, Z) → 2D (x, y) using perspective projection
    projected_2D = np.dot(camera_matrix, camera_coords.T).T
    
    # Normalize by dividing by depth (Z)
    projected_2D[:, 0] /= projected_2D
