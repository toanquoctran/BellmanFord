class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

def BellmanFord(s):
    dist[s] = 0
    for i in range(1, n):
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                dist[v] = dist[u] + w
                path[v] = u
    for i in range(m):
        u = graph[i].source
        v = graph[i].target
        w = graph[i].weight
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False
    return True

if __name__ == "__main__":
    INF = 10**9
    c = int(input())
    for _ in range(c):
        dist = [INF for _ in range(999999)]
        path = [-1 for _ in range(999999)]
        graph = []
        n, m = map(int, input().split())
        for _ in range(m):
            x, y, t = map(int, input().split())
            graph.append(Edge(x, y, t))
        res = BellmanFord(0)
        if not res:
            print("possible")
        else:
            print("not possible")