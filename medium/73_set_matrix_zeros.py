class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.add((i,j))

        done_rows = set()
        done_cols = set()

        for i,j in zeros:
            # fix col:
            if j not in done_cols:
                for row in range(len(matrix)):
                    matrix[row][j] *= 0

            # fix row
            if i not in done_rows:
                for col in range(len(matrix[0])):
                    matrix[i][col] *= 0

"""
Idea:
- find all cells with zeros
- for each found zero update row and col without repeat due to done sets
"""