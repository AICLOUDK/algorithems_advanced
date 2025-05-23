# python3
from itertools import combinations

def read_graph():
    n, m = map(int, input().split())
    g = [[float('inf')] * n for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1; v -= 1
        g[u][v] = g[v][u] = w
    return n, g

def tsp(g):
    n = len(g)
    size = 1 << n
    dist = [[float('inf')] * n for _ in range(size)]
    parent = [[-1] * n for _ in range(size)]
    dist[1][0] = 0
    for mask in range(size):
        for u in range(n):
            if dist[mask][u] == float('inf'):
                continue
            for v in range(n):
                if mask & (1 << v) or g[u][v] == float('inf'):
                    continue
                next_mask = mask | (1 << v)
                cost = dist[mask][u] + g[u][v]
                if cost < dist[next_mask][v]:
                    dist[next_mask][v] = cost
                    parent[next_mask][v] = u
    min_cost = float('inf')
    end_node = -1
    full_mask = size - 1
    for v in range(1, n):
        total_cost = dist[full_mask][v] + g[v][0]
        if total_cost < min_cost:
            min_cost = total_cost
            end_node = v
    if min_cost == float('inf'):
        return -1, []
    path = []
    mask = full_mask
    current = end_node
    while current != -1:
        path.append(current)
        prev = parent[mask][current]
        mask ^= (1 << current)
        current = prev
    path.reverse()
    return min_cost, path

if __name__ == '__main__':
    n, g = read_graph()
    total_cost, path = tsp(g)
    print(total_cost)
    print(' '.join(str(node + 1) for node in path))