class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        visited = [False] * n

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)    
        
        def dfs(node):
            for nbr in adj[node]:
                if not visited[nbr]:
                    visited[nbr] = True
                    dfs(nbr)
        res = 0

        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res += 1

        return res

