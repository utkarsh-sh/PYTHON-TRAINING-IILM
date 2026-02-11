import heapq

def prim_algorithm(graph, V):
    visited = [False] * V
    min_heap = [(0, 0)]  # (weight, vertex)
    mst_cost = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        mst_cost += weight

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                mst_edges.append((u, v, w))

    return mst_edges, mst_cost

# Example usage
if __name__ == "__main__":
    V = 5
    graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8)],
        4: [(1, 5), (2, 7)]
    }

    mst_edges, cost = prim_algorithm(graph, V)
    print("Edges in Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"{u} -- {v} == {weight}")
    print(f"Total cost of MST: {cost}")
