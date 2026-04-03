import math
import random
import time

# 🛰️ Satellite object
satellite = {
    "x": 0,
    "y": 0,
    "vx": 1,
    "vy": 1
}

# ☄️ Create random debris
debris_list = []
for i in range(5):
    debris_list.append({
        "x": random.randint(-20, 20),
        "y": random.randint(-20, 20)
    })

SAFE_DISTANCE = 5

# 📏 Distance calculation
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 🚨 Collision avoidance logic
def avoid_collision():
    print("⚠️ Collision Risk Detected! Adjusting satellite path...")
    satellite["vx"] += random.choice([-1, 1])
    satellite["vy"] += random.choice([-1, 1])

# 🔁 Simulation loop
print("🚀 Starting SafeOrbit AI Simulation...\n")

for step in range(20):
    print(f"🔹 Step {step + 1}")

    # Move satellite
    satellite["x"] += satellite["vx"]
    satellite["y"] += satellite["vy"]

    print(f"Satellite Position: ({satellite['x']}, {satellite['y']})")

    # Check against each debris
    for i, debris in enumerate(debris_list):
        distance = calculate_distance(
            satellite["x"], satellite["y"],
            debris["x"], debris["y"]
        )

        print(f"Distance to debris {i+1}: {round(distance, 2)}")

        # If too close → avoid
        if distance < SAFE_DISTANCE:
            avoid_collision()

    print("-" * 40)
    time.sleep(1)

print("\n✅ Simulation Completed Successfully!")