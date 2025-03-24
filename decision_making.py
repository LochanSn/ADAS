import json
import numpy as np
import time

# Define thresholds (seconds)
WARNING_ZONE_TTC = 4.0  # Alert threshold
CRITICAL_ZONE_TTC = 2.0  # Automated action threshold

def load_sensor_data():
    """
    Simulate loading sensor fusion data from `object_detection.py`.
    The real implementation should read this from an actual source.
    """
    try:
        with open("sensor_data.json", "r") as file:
            return json.load(file)  # Load object data
    except FileNotFoundError:
        print("Error: No object detection data found.")
        return []

def calculate_ttc(distance, relative_speed):
    """
    Compute Time-to-Collision (TTC).
    If relative speed is zero or negative, return a high value (no collision risk).
    """
    if relative_speed <= 0:
        return float("inf")
    return distance / relative_speed

def assess_risk_and_act(objects):
    """
    Analyze objects and determine appropriate collision avoidance actions.
    """
    for obj in objects:
        obj_type = obj["type"]
        distance = obj["distance"]  # Meters
        relative_speed = obj["relative_speed"]  # m/s

        ttc = calculate_ttc(distance, relative_speed)

        if ttc < CRITICAL_ZONE_TTC:
            print(f"🚨 CRITICAL: {obj_type} detected at {distance}m! Activating Emergency Braking!")
            apply_braking()
        elif ttc < WARNING_ZONE_TTC:
            print(f"⚠ WARNING: {obj_type} at {distance}m. Issuing alert!")
            trigger_alert()
        else:
            print(f"✅ Safe: {obj_type} at {distance}m.")

def apply_braking():
    """Simulate emergency braking action."""
    print("🛑 Braking System Activated!")
    time.sleep(1)  # Simulate response time
    print("✔ Braking completed.")

def trigger_alert():
    """Simulate visual/audio warning alert."""
    print("🔊 Warning: Object detected ahead!")
    time.sleep(0.5)

if __name__ == "__main__":
    detected_objects = load_sensor_data()
    if detected_objects:
        assess_risk_and_act(detected_objects)
    else:
        print("No objects detected. Drive safe!")