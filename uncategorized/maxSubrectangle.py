import heapq as hq

# x = [[2,1,-3,-4,5],[0,6,3,4,1],[2,-2,-1,4,-5],[-3,3,1,0,3]]
x = [[7,-100,2,2,2],
     [1000,-1,2,2,1000],
     [-100,-100,2,2,2]]
n = len(x)
m = len(x[0])
print(sum(x[1]))

q = []

class Solution:

    def __init__(self) -> None:
        self.checked = set()
        self.maxSum = -99999999999999

    def getMaxSide(self,top,bottom,left,right):
        topSum,bottomSum,leftSum,rightSum = (-9999999999999,0,[]),(-9999999999999,0,[]),(-9999999999999,0,[]),(-9999999999999,0,[])
        
        if top > 0:
            topSum = (sum(x[top-1][left:right+1]), 1, [(top-1,c) for c in range(left,right+1)])

        if bottom < n-1:
            bottomSum = (sum(x[bottom+1][left:right+1]), 2, [(bottom+1,c) for c in range(left,right+1)])

        if right < m-1:
            s = 0
            for i in range(top,bottom+1):
                s += x[i][right+1]

            rightSum = (s, 3, [(r,right+1) for r in range(top,bottom+1)])

        if left > 0:
            s = 0
            for i in range(top,bottom+1):
                s += x[i][left-1]
            leftSum = (s, 4, [(r,left-1) for r in range(top,bottom+1)])

        return max(topSum,bottomSum,leftSum,rightSum)

    def maxSubRect(self):
        for r, row in enumerate(x):
            for c,elem in enumerate(row):
                if elem > 0:
                    hq.heappush(q, (-elem,r,c))

        while q:
            val,r,c = hq.heappop(q)
            val *= -1

            if (r,c) in self.checked:
                continue

            self.checked.add((r,c))

            currSum = val
            top,bottom = r,r
            left,right = c,c

            while True:

                sideSum,side,seenCells = self.getMaxSide(top,bottom,left,right)

                if sideSum >= 0:

                    currSum += sideSum

                    if side == 1:
                        top -= 1
                    elif side == 2:
                        bottom += 1
                    elif side == 3:
                        right += 1
                    elif side == 4:
                        left -= 1
                    
                    for cell in seenCells:
                        self.checked.add(cell)

                else:
                    self.maxSum = max(self.maxSum, currSum)
                    break

        return self.maxSum


s1 = Solution()
print(f"maxSum = {s1.maxSubRect()}")


