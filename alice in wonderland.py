def BellmanFord(s):
    dist[s][s] = 0
    for _ in range(1, n):        
        for u, v, w in graph:           
            if dist[s][u] != inf and dist[s][v] > dist[s][u] + w:
                dist[s][v] = dist[s][u] + w
    for _ in range(1, n):
        for u, v, w in graph:
            if dist[s][u] != inf and dist[s][u] + w < dist[s][v]:
                dist[s][v] = -inf
    
if __name__ == "__main__":
    inf = (2**30 + 1) * 100 + 1
    tc = 0
    while True:
        n = int(input())
        dist = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
        graph = []  
        monuments = []   
        if n == 0:
            break
        tc += 1     
        for i in range(n):
            lines = list(input().split())
            monuments.append(lines[0])
            for j in range(n):
                w = int(lines[j + 1])
                if w == 0 and i != j:
                    continue
                if w >= 0 and i == j:
                    w = 0
                graph.append((i, j, w))
        q = int(input())
        print("Case #{}:".format(tc))
        for i in range(n):
            BellmanFord(i)      
        for _ in range(q):
            u, v = map(int, input().split())
            if dist[u][v] >= inf:
                print("{}-{} NOT REACHABLE".format(monuments[u], monuments[v]))
            elif dist[u][v] <= -inf:
                print("NEGATIVE CYCLE")
            else:
                print("{}-{} {}".format(monuments[u], monuments[v], dist[u][v]))