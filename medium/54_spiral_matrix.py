class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        top, left, right, bottom = 0,0,m-1,n-1
        size = n*m

        res = []

        while True:
            # top
            res.extend(matrix[top][left:right+1])
            top += 1
            if len(res) == size:
                return res

            # right 
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -= 1
            if len(res) == size:
                return res

            # bottom
            for i in range(right,left-1,-1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if len(res) == size:
                return res

            # left
            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left += 1
            if len(res) == size:
                return res

"""
idea:
add values to resulting array in a spiral
after each row/col move in the wall
"""