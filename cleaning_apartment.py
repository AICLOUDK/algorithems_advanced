# python3
import itertools

def var(i, j):
    return n * i + j

def algo(literals, clauses):
    clauses.append(literals)
    clauses.extend([-l, -k] for l, k in itertools.combinations(literals, 2))
    return clauses

def seg(n, edges):
    clauses = []
    st = [[] for _ in range(n)]
    for i, j in edges:
        st[i-1].append(j-1)
        st[j-1].append(i-1)
    positions = range(1, n+1)
    for i in range(n):
        clauses = algo([var(i, j) for j in positions], clauses)
    for j in positions:
        clauses = algo([var(i, j) for i in range(n)], clauses)
    for j in positions[:-1]:
        for i, nodes in enumerate(st):
            clauses.append([-var(i, j)] + [var(node, j+1) for node in nodes])
    return clauses

if __name__ == '__main__':
    n, m = map(int, input().split())
    corridors = [list(map(int, input().split())) for _ in range(m)]
    clause = seg(n, corridors)
    print(len(clause), n * n)
    for c in clause:
        c.append(0)
        print(' '.join(map(str, c)))