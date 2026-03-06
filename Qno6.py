import math
import heapq

# safety probability table
graph = {
    "KTM": [("JA", 0.90), ("JB", 0.80)],
    "JA": [("KTM", 0.90), ("PH", 0.95), ("BS", 0.70)],
    "JB": [("KTM", 0.80), ("JA", 0.60), ("BS", 0.90)],
    "PH": [("JA", 0.95), ("BS", 0.85)],
    "BS": [("JA", 0.70), ("JB", 0.90), ("PH", 0.85)]
}

def safest_path(graph, source):
    dist = {v: float('inf') for v in graph}
    parent = {v: None for v in graph}

    dist[source] = 0
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)

        for v, prob in graph[u]:
            weight = -math.log(prob)
            new_dist = dist[u] + weight

            # Modified RELAX
            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = u
                heapq.heappush(pq, (new_dist, v))

    return dist, parent


def get_path(parent, target):
    path = []
    while target:
        path.append(target)
        target = parent[target]
    return path[::-1]


source = "KTM"
dist, parent = safest_path(graph, source)

print("Safest paths from KTM:\n")

for node in graph:
    path = get_path(parent, node)

    if node != source:
        probability = math.exp(-dist[node])
    else:
        probability = 1

    print(f"{source} → {node}")
    print("Path:", " -> ".join(path))
    print("Safety Probability:", round(probability, 4))
    print()
    