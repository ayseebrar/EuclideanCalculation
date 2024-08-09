import math

# Noktaların tanımlanması
points = [(2, 3), (4, 8), (6, 1), (7, 7), (5, 5)]

# Öklid mesafesi için fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# Minimum mesafenin bulunması
min_distance = min(distances)
print(f"Minimum Öklid mesafesi: {min_distance}")
