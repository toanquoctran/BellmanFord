class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
        
def BellmanFord(s):
    dist = [-INF for _ in range(n + 1)]
    dist[s] = 0
    for _ in range(1, n):
        for i in range(m):
            u = graph[i].source
            v = graph[i].target
            w = graph[i].weight
            if dist[u] != -INF and dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
    for _ in range(1, n):
        for i in range(m):
            u = graph[i].source
            v = graph[i].target
            w = graph[i].weight
            if dist[u] != -INF and dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
                if v == s:
                    return True
    return False

if __name__ == "__main__":
    INF = int(1e9)
    t = int(input())
    for _ in range(t):
        graph = []
        n, m = map(int, input().split())
        visited = [False for _ in range(n + 1)]
        for _ in range(m):
            i, j, c = map(int, input().split())
            graph.append(Edge(i, j, c))
        if BellmanFord(1):
            print("Yes")
        else:
            print("No")