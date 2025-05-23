# python 3
import itertools

def v(i, var):
    return 3 * (i - 1) + var

def algort(i):
    lits = [v(i, var) for var in range(1, 4)]
    clauses = [lits]
    clauses += [[-l1, -l2] for l1, l2 in itertools.combinations(lits, 2)]
    return clauses

def part(i, j):
    return [[-v(i, var), -v(j, var)] for var in range(1, 4)]

def segment(n, edges):
    clauses = []
    for i in range(1, n + 1):
        clauses += algort(i)
    for i, j in edges:
        clauses += part(i, j)
    return clauses

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    clauses = segment(n, edges)
    print(len(clauses), n * 3)
    for c in clauses:
        c.append(0)
        print(' '.join(map(str, c)))