points = [(1, 2), (4, 6), (7, 1), (2, 3), (5, 5)]

def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances) if distances else None

print(min_distance)
