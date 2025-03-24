import numpy as np
import cv2

class KalmanTracker:
    def __init__(self):
        # Create Kalman filter
        self.kf = cv2.KalmanFilter(4, 2)  # 4 state variables (x, y, dx, dy) and 2 measurements (x, y)

        # State transition matrix (Assuming constant velocity model)
        self.kf.transitionMatrix = np.array([[1, 0, 1, 0], 
                                             [0, 1, 0, 1], 
                                             [0, 0, 1, 0], 
                                             [0, 0, 0, 1]], np.float32)

        # Measurement matrix (How we observe the state)
        self.kf.measurementMatrix = np.array([[1, 0, 0, 0], 
                                              [0, 1, 0, 0]], np.float32)

        # Process noise covariance (Small values for smooth predictions)
        self.kf.processNoiseCov = np.array([[1, 0, 0, 0], 
                                            [0, 1, 0, 0], 
                                            [0, 0, 1, 0], 
                                            [0, 0, 0, 1]], np.float32) * 0.03

        # Measurement noise covariance (Tune based on sensor accuracy)
        self.kf.measurementNoiseCov = np.array([[1, 0], 
                                                [0, 1]], np.float32) * 0.1

        # Initial state estimate
        self.kf.statePre = np.array([[0], [0], [0], [0]], np.float32)

    def update(self, measurement):
        """Update tracker with new detection."""
        self.kf.correct(np.array([[measurement[0]], [measurement[1]]], np.float32))

    def predict(self):
        """Predict next position."""
        predicted = self.kf.predict()
        return int(predicted[0]), int(predicted[1])  # Return (x, y)
    

# Example Radar-to-Camera projected positions (from Step 2)
detections = [(700, 350), (650, 400), (750, 370)]  # Example object locations

# Initialize trackers for detected objects
trackers = [KalmanTracker() for _ in detections]

# Simulating tracking over 5 frames
for frame in range(5):
    print(f"\nFrame {frame + 1}")

    for i, detection in enumerate(detections):
        trackers[i].update(detection)  # Update tracker with new detection
        predicted_pos = trackers[i].predict()  # Predict next position

        print(f"Object {i + 1}: Measured {detection}, Predicted {predicted_pos}")
