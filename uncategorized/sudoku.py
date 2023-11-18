from copy import deepcopy

class Solution:
    def __init__(self, board):
        self.board = board
    def getBox(self,r,c):
        return (((r-1)//3)*3 + (c-1)//3) + 1
    
    def check(self):
        # correct = [1,2,3,4,5,6,7,8,9]

        # # check rows
        # b1 = deepcopy(self.board)
        # for row in b1:
        #     row.sort()
        #     if row != correct:
        #         return False

        # # check cols
        # transpose = self.getTranspose()
        # for col in transpose:
        #     col.sort()
        #     if col != correct:
        #         return False
            
        # #check boxs
        # b3 = deepcopy(self.board)
        # for r in range(0,9,3):
        #     for c in range(0,9,3):
        #         res = []
        #         for row in range(r,r+3):
        #             for col in range(c,c+3):
        #                 res.append(b3[row][col])

        #         res.sort()
        #         if res != correct:
        #             return False
                
        # return True
        ans = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
        correct = ans == self.board

        if not correct:
            print("Not 100%")

        partiallyCorrect = True
        for r,row in enumerate(self.board):
            for c, elem in enumerate(row):
                if elem != '.' and elem != ans[r][c]:
                    partiallyCorrect = False
                    break

        if partiallyCorrect:
            print("incomplete but so far correct")
        else:
            print("incorrecttt!!!")



    def getTranspose(self):
        transpose = [[] for i in range(9)]
        for r in range(9):
            for c in range(9):
                transpose[(r*9 + c) % 9].append(self.board[r][c])
        return transpose
    

    def solveSudoku(self):

        transpose = self.getTranspose()

        optionBoard = deepcopy(self.board)
        for r in range(9):
            for c in range(9):
                if optionBoard[r][c] == '.':
                    optionBoard[r][c] = []

        for n in range(1,10):
            n = str(n)
            rowsLacking = []
            colsLacking = []
            boxsLacking = []

            for i, row in enumerate(self.board):
                if n not in row:
                    rowsLacking.append(i+1)

            for i, col in enumerate(transpose):
                if n not in col:
                    colsLacking.append(i+1)

            for r in range(0,9,3):
                for c in range(0,9,3):
                    found = False
                    for row in range(r,r+3):
                        for col in range(c,c+3):
                            if self.board[row][col] == n:
                                found = True
                                break
                        
                        if found:
                            break

                    if not found:                          
                        boxsLacking.append(r + c//3 +1)

            # print(f"{n} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            # print(f"rows: {rowsLacking}")
            # print(f"cols: {colsLacking}")
            # print(f"boxs: {boxsLacking}")


            for row in rowsLacking:
                for col in range(1,10):
                    currBox = self.getBox(row,col)
                    if board[row-1][col-1] == '.' and col in colsLacking and currBox in boxsLacking:
                        #good place n in cell
                        optionBoard[row-1][col-1].append(n)

        # self.printBoard(optionBoard)

        for r in range(9):
            for c in range(9):
                if type(optionBoard[r][c]) == list and len(optionBoard[r][c]) == 1:
                    val = optionBoard[r][c][0]
                    optionBoard[r][c] = val
                    self.board[r][c] = val

        print("filled with certains: ")

        self.printBoard(self.board)


    def printBoard(self,b):
        print("    ",end='')
        for x in range(1,10):
            print(f"{x} ",end='')
        print("\n----------------------")
        for i,row in enumerate(b):
            print(f"{i+1} | ",end="")
            for c in row:
                print(c,end = " ")
            print("")





ans = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
boardOg = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]




s1 = Solution(board)
print("og: ============================")
s1.printBoard(boardOg)
s1.solveSudoku()

# s1.printBoard(board)
print("ans ============================")
s1.printBoard(ans)

s1.check()