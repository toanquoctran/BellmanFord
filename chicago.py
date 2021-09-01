class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

def BellmanFord(s):
    dist[s] = 1
    for i in range(1, n):
        for j in range(len(graph)):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if dist[u] != -INF and dist[u] * w > dist[v]:
                dist[v] = dist[u] * w

if __name__ == "__main__":
    while True:
        lines = list(map(int, input().split()))      
        if lines[0] == 0:
            break
        INF = int(1e9)
        graph = []
        n = lines[0]
        m = lines[1]
        dist = [-INF for _ in range(n + 1)]
        for _ in range(m):
            a, b, p = map(int, input().split())
            p = p / 100
            graph.append(Edge(a, b, p))
            graph.append(Edge(b, a, p))
        res = BellmanFord(1)
        print("{:.6f} percent".format(dist[n]*100))