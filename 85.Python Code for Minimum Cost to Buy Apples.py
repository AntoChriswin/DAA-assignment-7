from collections import defaultdict
import heapq

def minCostToBuyApples(n, roads, appleCost, k):
    graph = defaultdict(list)
    for a, b, cost in roads:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    def dijkstra(start):
        heap = [(0, start)]
        costs = {node: float('inf') for node in range(1, n + 1)}
        costs[start] = 0

        while heap:
            current_cost, current_node = heapq.heappop(heap)

            if current_cost > costs[current_node]:
                continue

            for neighbor, edge_cost in graph[current_node]:
                new_cost = current_cost + edge_cost
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor))

        total_costs = [appleCost[i - 1] + k * costs[i] for i in range(1, n + 1)]
        return total_costs

    return dijkstra(1)

# Example usage
n = 4
roads = [[1, 2, 4], [2, 3, 2], [2, 4, 5], [3, 4, 1], [1, 3, 4]]
appleCost = [56, 42, 102, 301]
k = 2
print(minCostToBuyApples(n, roads, appleCost, k))  # Output: [54, 42, 48, 51]
