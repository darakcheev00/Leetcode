class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.count = 0
        for r in range(self.m):
            for c in range(self.n):
                if self.grid[r][c] == "1":
                    self.dfs(r,c)
                    self.count += 1
        
        return self.count

    def dfs(self,r,c):
        if self.grid[r][c] == "0" or self.grid[r][c] == "-1":
            return

        self.grid[r][c] = "-1"

        if r-1 >= 0:
            self.dfs(r-1,c)

        if r+1 < self.m:
            self.dfs(r+1,c)

        if c-1 >= 0:
            self.dfs(r,c-1)

        if c+1 < self.n:
            self.dfs(r,c+1)
        

"""
Time: O(m*n)
Space: O(1) no extra space used

Solution:
Run dfs on each cell in the grid. When a cell is visited mark it with -1.
Each time dfs ends that means one island is found.
"""
        