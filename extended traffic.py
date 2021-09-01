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
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for i in range(1, n):
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF

if __name__ == "__main__":
    t = int(input())
    INF = int(1e9)
    for case in range(t):
        graph = []
        dist = [INF for _ in range(99999)]
        input()
        n = int(input())
        junctionsBusyness = list(map(int, input().split()))
        m = int(input())
        for _ in range(m):
            s, d = map(int, input().split())
            w = (junctionsBusyness[d-1] - junctionsBusyness[s-1])**3
            graph.append(Edge(s, d, w))
        q = int(input())
        BellmanFord(1)
        print("Case {}:".format(case + 1))
        for i in range(q):
            junctionNumber = int(input())
            if dist[junctionNumber] < 3 or dist[junctionNumber] == INF:
                print("?")
            else:
                print(dist[junctionNumber])