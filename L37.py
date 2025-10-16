import math

# Input angle in degrees
angle_deg = float(input("Enter the angle in degrees: "))

# Convert degrees to radians
angle_rad = math.radians(angle_deg)

# Calculate sine, cosine, and tangent
sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)

# Display results
print(f"Sine({angle_deg}°) = {sin_value}")
print(f"Cosine({angle_deg}°) = {cos_value}")
print(f"Tangent({angle_deg}°) = {tan_value}")

