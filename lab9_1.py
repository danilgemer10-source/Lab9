import math

x = (-2, 5, 6)
y = (5, -3, 0.5)

distances = []

A = (-2, 5)
B = (5, -3)
C = (6, 0.5)

dAB = math.sqrt((x[1] - x[0])**2 + (y[1] - y[0])**2)
dBC = math.sqrt((x[2] - x[1])**2 + (y[2] - y[1])**2)

distances.append(dAB)
distances.append(dBC)

print(distances)
