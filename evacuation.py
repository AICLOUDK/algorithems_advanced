# python3
from collections import deque

def max_flow(n, edges, source, sink):
    graph = [[] for _ in range(n)]
    for u, v, c in edges:
        u -= 1
        v -= 1
        graph[u].append([v, c, len(graph[v])])
        graph[v].append([u, 0, len(graph[u]) - 1])

    flow = 0

    def bfs():
        level = [-1] * n
        level[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v, cap, rev in graph[u]:
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level

    def send_flow(u, sink, flow_in, level, it):
        if u == sink:
            return flow_in
        while it[u] < len(graph[u]):
            v, cap, rev = graph[u][it[u]]
            if cap > 0 and level[v] == level[u] + 1:
                pushed = send_flow(v, sink, min(flow_in, cap), level, it)
                if pushed > 0:
                    graph[u][it[u]][1] -= pushed
                    graph[v][rev][1] += pushed
                    return pushed
            it[u] += 1
        return 0

    while True:
        level = bfs()
        if level[sink] < 0:
            break
        it = [0] * n
        while True:
            pushed = send_flow(source, sink, float('inf'), level, it)
            if pushed <= 0:
                break
            flow += pushed
    return flow

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(max_flow(n, edges, 0, n - 1))