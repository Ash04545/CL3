import random

# Distance Matrix
dist = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

n = len(dist)
pheromone = [[1 for _ in range(n)] for _ in range(n)]

best_path = None
best_cost = float('inf')

for iteration in range(5):
    for ant in range(n):
        visited = [False] * n
        path = [ant]
        visited[ant] = True
        cost = 0

        current = ant

        while len(path) < n:
            next_city = None
            max_pheromone = -1

            for city in range(n):
                if not visited[city] and pheromone[current][city] > max_pheromone:
                    max_pheromone = pheromone[current][city]
                    next_city = city

            path.append(next_city)
            visited[next_city] = True
            cost += dist[current][next_city]
            current = next_city

        cost += dist[current][path[0]]
        path.append(path[0])

        if cost < best_cost:
            best_cost = cost
            best_path = path

        # Update pheromone
        for i in range(len(path) - 1):
            pheromone[path[i]][path[i+1]] += 1 / cost

print("Best Path:", best_path)
print("Minimum Cost:", best_cost)
