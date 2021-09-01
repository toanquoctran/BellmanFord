class Edge:
    def __init__(self, source, target):
        self.source = source
        self.target = target

def dfs(s, d):
    visited[s] = True
    if s == d:
        return True
    for edge in graph:
        u = edge.source
        v = edge.target
        if u == s:
            if not visited[v]:
                if dfs(v, d):
                    return True
    return False

def BellmanFord(s, d):
    dist[s] = 100
    for i in range(1, n):
        for j in range(len(graph)):
            u = graph[j].source
            v = graph[j].target
            if dist[u] > 0 and dist[u] + energy[v] > dist[v]:
                dist[v] = dist[u] + energy[v]
    for i in range(len(graph)):
        u = graph[i].source
        v = graph[i].target
        if dist[u] > 0 and dist[u] + energy[v] > dist[v] and dfs(u, d):
            return True
    if dist[d] > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        INF = int(1e9)
        n = int(input())
        dist = [-INF for _ in range(99999)]
        graph = []
        visited = [False for _ in range(99999)]
        energy = [0] * (n + 2)
        if n == -1:
            break
        for i in range(n):
            lines = list(map(int, input().split()))
            energy[i + 1] = lines[0]
            for j in range(2, 2 + lines[1]):
                graph.append(Edge(i + 1, lines[j]))
        if BellmanFord(1, n):
            print("winnable")
        else:
            print("hopeless")