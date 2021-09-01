class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

def BellmanFord(s):
    dist = [inf for _ in range(n + 1)]
    dist[0] = 0
    dist[s] = 0
    for _ in range(1, n):
        for i in range(len(graph)):
            u = graph[i].source
            v = graph[i].target
            w = graph[i].weight
            if dist[u] != inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return max(dist)
    
if __name__ == "__main__":
    inf = int(1e9)
    n = int(input())
    graph = []
    a = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(2, n + 1):
        lines = list(input().split())
        for j in range(1, len(lines) + 1):
            if lines[j - 1] != "x":
                graph.append(Edge(j, i, int(lines[j - 1])))
                graph.append(Edge(i, j, int(lines[j - 1])))
    print(BellmanFord(1))