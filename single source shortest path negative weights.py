class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
        
# def dfs(s, d):
#     visited[s] = True
#     if s == d:
#         return True
#     for edge in graph:
#         u = edge.source
#         v = edge.target
#         if u == s:
#             if not visited[v]:
#                 if dfs(v, d):
#                     return True
#     return False

def BellmanFord(s):
    dist[s] = 0
    for i in range(1, n):
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for _ in range(1, n):
        for i in range(m):
            u = graph[i].source
            v = graph[i].target
            w = graph[i].weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF

if __name__ == "__main__":
    INF = int(1e9)
    while True:
        n, m, q, s = map(int, input().split())
        dist = [INF for _ in range(n + 1)]
        graph = []
        visited = [False for _ in range(n + 1)]
        if n == 0 and m == 0 and q == 0 and s == 0:
            break
        for _ in range(m):
            u, v, w = map(int, input().split())
            graph.append(Edge(u, v, w))
        BellmanFord(s)
        for _ in range(q):
            t = int(input())
            if dist[t] == INF:
                print("Impossible")
            elif dist[t] == -INF:
                print("-Infinity")
            else:
                print(dist[t])
        print()