class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or len(board)==0:
            return False

        self.board = board
        self.word = word

        for i in range(len(board)):
            for j in range(len(board[0])):
                letter = board[i][j]
                if letter == word[0]:
                    seen = {(i,j)}
                    if self.search(i,j,1,seen):
                        return True
        return False

    def search(self,i,j,k,seen):
        if k == len(self.word):
            return True

        up,down,left,right = False, False, False, False
        if i-1 >= 0 and (i-1,j) not in seen and self.word[k] == self.board[i-1][j]:
            # print('up')
            up_set = seen.union({(i-1,j)})
            up = self.search(i-1,j,k+1,up_set)
        if i+1 < len(self.board) and (i+1,j) not in seen and self.word[k] == self.board[i+1][j]:
            # print('down')
            down_set = seen.union({(i+1,j)})
            down = self.search(i+1,j,k+1,down_set)
        if j-1 >= 0 and (i,j-1) not in seen and self.word[k] == self.board[i][j-1]:
            # print('left')
            left_set = seen.union({(i,j-1)})
            left = self.search(i,j-1,k+1,left_set)
        if j+1 < len(self.board[0]) and (i,j+1) not in seen and self.word[k] == self.board[i][j+1]:
            # print('right')
            right_set = seen.union({(i,j+1)})
            right = self.search(i,j+1,k+1,right_set)

        return up or down or left or right


"""
Idea:
Check each cell for first letter of word.
If match found then bfs into from that index looking for word

Notes:
Make sure all are if's (not elif's) so that all paths are checked
Use set.union to create new set instead of modifying current set
"""