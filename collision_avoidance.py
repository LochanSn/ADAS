import numpy as np

# Example detected objects (from sensor fusion & tracking)
detections = [
    {"label": "Car", "distance": 18, "speed": 3},  
    {"label": "Pedestrian", "distance": 8, "speed": 1},  
    {"label": "Bike", "distance": 25, "speed": 6}  
]

# Ego vehicle speed (speed of your vehicle)
ego_speed = 10  # m/s

# Define collision risk thresholds
TTC_THRESHOLD_WARNING = 3.0  # seconds (caution alert)
TTC_THRESHOLD_BRAKE = 2.0    # seconds (gentle braking)
TTC_THRESHOLD_EMERGENCY = 1.0 # seconds (emergency braking)

def compute_ttc(distance, obj_speed, ego_speed):
    """Calculate Time-to-Collision (TTC)"""
    relative_speed = abs(ego_speed - obj_speed)  # Speed difference
    if relative_speed == 0:  # Avoid division by zero
        return float('inf')
    
    return distance / relative_speed  # TTC in seconds

def determine_action(ttc):
    """Determine vehicle action based on TTC"""
    if ttc > TTC_THRESHOLD_WARNING:
        return "✅ Safe - No Action"
    elif TTC_THRESHOLD_BRAKE < ttc <= TTC_THRESHOLD_WARNING:
        return "⚠️ Warning: Slow Down"
    elif TTC_THRESHOLD_EMERGENCY < ttc <= TTC_THRESHOLD_BRAKE:
        return "🚨 Collision Likely: Apply Gentle Braking"
    else:
        return "🔥 EMERGENCY BRAKE ACTIVATED!"

# Process each detected object
for obj in detections:
    ttc = compute_ttc(obj["distance"], obj["speed"], ego_speed)
    action = determine_action(ttc)
    
    print(f"Object: {obj['label']} | Distance: {obj['distance']}m | TTC: {ttc:.2f}s | Action: {action}")
