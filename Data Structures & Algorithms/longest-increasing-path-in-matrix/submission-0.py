class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        mp = {}

        def dfs(r, c, prevval):
            if (r< 0 or c < 0 or r== rows or c== cols or matrix[r][c] <= prevval):
                return 0

            res = 1
            res = max(res, 1+ dfs(r+1, c, matrix[r][c]))
            res = max(res, 1+ dfs(r-1, c, matrix[r][c]))
            res = max(res, 1+ dfs(r, c+1, matrix[r][c]))
            res = max(res, 1+ dfs(r, c-1, matrix[r][c]))
            mp[(r,c)] = res
            return res

        for r in range(rows):
            for c in range(cols):
                dfs(r,c, -1)
        return max(mp.values())

            
        