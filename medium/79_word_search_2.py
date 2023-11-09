class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n,m = len(board),len(board[0])
        seen = set()
        res = False

        def backtrack(i,j,index):
            # print(board[i][j],seen,index,word)

            if index == len(word):
                # print("obama")
                res = True
                return

            first = word[index]
            u,d,l,r = False,False,False,False

            if (i-1,j) not in seen and i > 0 and board[i-1][j] == first:
                seen.add((i-1,j))
                backtrack(i-1,j,index+1)
                seen.remove((i-1,j))
            
            if (i+1,j) not in seen and i < n-1 and board[i+1][j] == first:
                seen.add((i+1,j))
                backtrack(i+1,j,index+1)
                seen.remove((i+1,j))

            if (i,j-1) not in seen and j > 0 and board[i][j-1] == first:
                seen.add((i,j-1))
                backtrack(i,j-1,index+1)
                seen.remove((i,j-1))

            if (i,j+1) not in seen and j < m-1 and board[i][j+1] == first:
                seen.add((i,j+1))
                backtrack(i,j+1,index+1)
                seen.remove((i,j+1))



        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0]:
                    seen.add((r,c))
                    backtrack(r,c,1)
                    seen.remove((r,c))

        return False
            