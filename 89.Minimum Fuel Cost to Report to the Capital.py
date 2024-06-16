def minFuelCost(roads, seats):
    graph = collections.defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node, parent):
        total = 0
        for nei in graph[node]:
            if nei != parent:
                total += dfs(nei, node)
        return max(1, total) * seats

    return dfs(0, -1) - seats
