

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_rows = len(heights)
        num_cols = len(heights[0])

        pacificSet = set()
        atlanticSet = set()

        def dfs(r,c,ocean):
            if (r,c) in ocean:
                return 

            ocean.add((r,c))

            currHeight = heights[r][c]
            if r-1 >= 0 and heights[r-1][c] >= currHeight:
                dfs(r-1,c,ocean)

            if r+1 < num_rows and heights[r+1][c] >= currHeight:
                dfs(r+1,c,ocean)

            if c-1 >= 0 and heights[r][c-1] >= currHeight:
                dfs(r,c-1,ocean)

            if c+1 < num_cols and heights[r][c+1] >= currHeight:
                dfs(r,c+1,ocean)
                
                
        for r in range(num_rows):
            dfs(r,0,pacificSet)

        for c in range(num_cols):
            dfs(0,c, pacificSet)

        for r in range(num_rows):
            dfs(r,num_cols-1, atlanticSet)

        for c in range(num_cols):
            dfs(num_rows-1,c, atlanticSet)

        both = pacificSet.intersection(atlanticSet)
        result = []
        for i in range(len(both)):
            tup = both.pop()
            result.append([tup[0],tup[1]])

        return result

"""
Time: O(m*n)
Space: O(m*n)

Idea start from pacific shore and make a set of cells that can be reached using dfs, not revisiting same cell using memoization.
Do the same for atlantic shore.
Return intersection of sets to get cells that reach both oceans.

"""
