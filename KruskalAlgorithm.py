class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal_algorithm(vertices, edges):
    # Sort edges based on weight
    edges.sort(key=lambda edge: edge[2])
    dsu = DisjointSet(vertices)

    mst = []
    mst_cost = 0

    for u, v, weight in edges:
        if dsu.union(u, v):
            mst.append((u, v, weight))
            mst_cost += weight

    return mst, mst_cost

# Example usage
if __name__ == "__main__":
    V = 4  # Number of vertices (0 to V-1)
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    mst_edges, cost = kruskal_algorithm(V, edges)
    print("Edges in Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"{u} -- {v} == {weight}")
    print(f"Total cost of MST: {cost}")
