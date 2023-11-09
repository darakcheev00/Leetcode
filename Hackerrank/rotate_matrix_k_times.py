from copy import deepcopy

def findAndReplace(r,c, dist, matrix, snapshot, top, bottom, left, right):
    x,y = r,c
    while dist > 0:
        # left side
        if c == left and r < bottom:
            rem = bottom - r
            if dist <= rem:
                r += dist
                dist = 0
            else:
                dist -= rem
                r = bottom

        # right side
        elif c == right and r > top:
            rem = r - top
            if dist <= rem:
                r -= dist
                dist = 0
            else:
                dist -= rem
                r = top

        # top side
        elif r == top and c > left:
            rem = c - left
            if dist <= rem:
                c -= dist
                dist = 0
            else:
                dist -= rem
                c = left
        
        # bottom side
        elif r == bottom and c < right:
            rem = right - c
            if dist <= rem:
                c += dist
                dist = 0
            else:
                dist -= rem
                c = right

    print(f"inserting {snapshot[x][y]} into {r,c}")
    matrix[r][c] = snapshot[x][y]



def rotateMatrix(matrix,k):
    m = len(matrix)
    n = len(matrix[0])

    maxSteps = min(m // 2, n // 2)
    top, left = 0, 0
    bottom, right = m-1, n-1

    snapshot = deepcopy(matrix)

    for i in range(maxSteps):
        top += i
        bottom -= i
        left += i
        right -= i

        m -= 2*i
        n -= 2*i

        perimeter = 2*m + 2*n - 4

        # top and bottom
        for col in range(left,right+1):
            findAndReplace(top, col,  k % perimeter, matrix, snapshot, top, bottom, left, right)
            findAndReplace(bottom, col,  k % perimeter, matrix, snapshot, top, bottom, left, right)

        # left and right
        for row in range(top,bottom+1):
            findAndReplace(row, left,  k % perimeter, matrix, snapshot, top, bottom, left, right)
            findAndReplace(row, right,  k % perimeter, matrix, snapshot, top, bottom, left, right)

    return matrix



matrix = [
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24]
]
answer = [
    [5,6,12,18,24,23],
    [4,17,16,15,14,22],
    [3,11,10,9,8,21],
    [2,1,7,13,19,20]
]
res = rotateMatrix(matrix,4)
    
for row in res:
    for elem in row:
        print(f"{elem}\t", end='')
    print('\n')
print(res == answer)

"""
ALGORITHM WORKS

idea is for each ring, for each cell break step of k steps into small parts, each being as long as the side length
"""
