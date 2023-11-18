class Solution:
    def snakesAndLadders(self, board) -> int:
        n = len(board)
        curr = 1          
        
        def translate(num):
            row = n-1 - ((num-1) // n)

            col = 0
            if ((num-1) // n) % 2 == 0:
                # even = from left
                col = ((num-1) % n)
            else:
                # odd = from right
                col = n-1 - ((num-1) % n)
            
            return row, col


        cache = {}

        def play(curr,path):

            if curr == n**2:
                return 0

            if curr in cache:
                print(f"already explored {curr}")
                return cache[curr]
            
            moves = []

            farthestFreeFound = False

            for candidate in range(min(curr+6, n**2), curr, -1):
                r,c = translate(candidate)
                # print(candidate,r,c)
                boardVal = board[r][c]
                
                if boardVal == -1 and not farthestFreeFound:
                    moves.append(candidate)
                    farthestFreeFound = True

                elif boardVal != -1 and boardVal != curr and boardVal not in path:
                    moves.append(boardVal)

                # if boardVal == -1:
                #     moves.append(candidate)
                # else:
                #     moves.append(boardVal)
                

            print(f"curr: {curr}, moves:{moves}")
            if len(moves) == 0:
                return 9999999999

            moveResults = []

            for move in moves:
                moveResults.append(play(move,path+[move]))

            minMoves = min(moveResults) + 1
            cache[curr] = minMoves
            print(f'done exploring from {curr}, minMoves = {minMoves}')
            return minMoves


        return play(1,[])
        
    

board = [[-1,4,-1],[6,2,6],[-1,3,-1]]
Solution.snakesAndLadders(Solution,board)


"""
try all ladders and snakes and farthest free cell that has no ladder
- dfs on all ladders and farthest free cell
"""