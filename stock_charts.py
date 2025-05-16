# python3
class StockCharts:
    def read_data(self):
        n, k = map(int, input().split())
        stock_data = [list(map(int, input().split())) for _ in range(n)]
        return n, k, stock_data

    def algort(self, stock1, stock2):
        return all(x > y for x, y in zip(stock1, stock2))

    def build_graph(self, n, stock_data):
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    if self.algort(stock_data[i], stock_data[j]):
                        graph[i].append(j)
        return graph

    def bpm(self, u, mr, seen, graph):
        for v in graph[u]:
            if not seen[v]:
                seen[v] = True
                if mr[v] == -1 or self.bpm(mr[v], mr, seen, graph):
                    mr[v] = u
                    return True
        return False

    def min_charts(self, n, stock_data):
        graph = self.build_graph(n, stock_data)
        mr = [-1] * n
        result = 0
        for u in range(n):
            seen = [False] * n
            if self.bpm(u, mr, seen, graph):
                result += 1
        return n - result

    def solve(self):
        n, k, stock_data = self.read_data()
        result = self.min_charts(n, stock_data)
        self.write_response(result)

    def write_response(self, result):
        print(result)

if __name__ == '__main__':
    stock_charts = StockCharts()
    stock_charts.solve()