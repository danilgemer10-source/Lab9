import math

x = (-2, 5, 6)
y = (5, -3, 0.5)

distances = []

for i in range(len(x) - 1):
    d = math.sqrt((x[i + 1] - x[i])**2 + (y[i + 1] - y[i])**2)
    distances.append(d)

print(distances)

