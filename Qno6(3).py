from collections import deque

# Graph capacities
graph = {
    "KTM": {"JA": 10, "JB": 15},
    "JA": {"PH": 8, "BS": 5},
    "JB": {"BS": 12, "JA": 4},
    "PH": {"BS": 6},
    "BS": {}
}

def bfs(residual, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()

        for v in residual[u]:
            if v not in visited and residual[u][v] > 0:
                parent[v] = u
                visited.add(v)
                queue.append(v)

                if v == sink:
                    return True
    return False


def edmonds_karp(graph, source, sink):
    residual = {u: dict(v) for u, v in graph.items()}

    # add reverse edges
    for u in graph:
        for v in graph[u]:
            if v not in residual:
                residual[v] = {}
            if u not in residual[v]:
                residual[v][u] = 0

    parent = {}
    max_flow = 0
    step = 1

    while bfs(residual, source, sink, parent):

        # find bottleneck flow
        path_flow = float("inf")
        s = sink
        path = []

        while s != source:
            path.insert(0, s)
            path_flow = min(path_flow, residual[parent[s]][s])
            s = parent[s]
        path.insert(0, source)

        print(f"Step {step}")
        print("Augmenting Path:", " -> ".join(path))
        print("Flow Added:", path_flow)

        # update residual capacities
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow
        step += 1
        print()

    print("Maximum Flow =", max_flow)

source = "KTM"
sink = "BS"

edmonds_karp(graph, source, sink)