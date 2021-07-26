import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = []
        n = len(grid)
        for i in range(n):
            row.append(max(grid[i]))
        arr = np.array(grid)
        arr_trans = arr.transpose()
        col = []
        for i in range(n):
            col.append(max(arr_trans[i]))
        su = 0
        for i in range(n):
            for j in range(n):
                su += min(row[i],col[j]) - grid[i][j]
        return su