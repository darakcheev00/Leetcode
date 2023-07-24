# sliding window maximum
"""
Return the maximum number in the window of size k
as it slides across the array.
"""
import heapq as hq

class Node:
    def __init__(self,val):
        self.val = val
        self.count = 1

    def __lt__(self,other):
        return self.val > other.val

    def __str__(self):
        return "("+str(self.val)+","+str(self.count)+")"

class Manager:
    def __init__(self,k):
        self.heap = []
        self.map = {}
        self.k = k

    def IncreaseOrCreate(self,val):
        if val in self.map:
            self.map[val].count += 1
        else:
            newNode = Node(val)
            self.map[val] = newNode
            # add to heap
            # print("before")
            # self.printHeap()
            hq.heappush(self.heap, newNode)
            # print("after")
            # self.printHeap()

    def decreaseOrDelete(self,val):
        if val not in self.map:
            print("error")
            return -1

        self.map[val].count -= 1

        if self.map[val].count == 0:
            self.map.pop(val)

    def printHeap(self):
        for i in self.heap:
            print(i, end="")
        print("")

    def printMap(self):
        for i,val in self.map.items():
            print(str(i)+", ", end = "")

    def print(self):
        self.printHeap()
        self.printMap()
        print("\n")


    def getMax(self):
        while self.heap[0].count == 0:
            hq.heappop(self.heap)
        return self.heap[0].val

    
class Solution:
    def sliding_window_maximum(self,nums,k):
        res = []
        currMax = -999999999999
        manager = Manager(k)

        for i,n in enumerate(nums):
            # counter
            manager.IncreaseOrCreate(n)

            if i > k-1:
                # pop oldest
                out_num = nums[i-k]
                manager.decreaseOrDelete(out_num)
                # manager.print()
                if out_num < currMax:
                    # regular case: check if new incoming is greater
                    currMax = max(currMax,n)

                else:
                    # leaving number is equal to the max
                    # so either the max is now lower or equal to the old max (because a duplicate exists)
                    currMax = manager.getMax()


                res.append(currMax)

            else:
                # during the start when the window is filling up with k elements
                currMax = max(currMax,n)
                # manager.print()
                if i == k-1:
                    res.append(currMax)
                
            # print(f"added {currMax}")
        
        return res

dq = 4
nums1 = [1,3,-1,-3,5,3,6,7]
i = 5
res - 3,3,5,

expected1 = [3,3,5,5,6,7]

nums2 = [1,3,-1,-3,2,1,3,6,7]
expected2 = [3,3,2,2,3,6,7]

nums3 = [9,8,7,6,5,4,3,2,1]
expected3 = [9,8,7,6,5,4,3]

nums4 = [1,2,3,4,1,4,-1,5,3,5]
expected4 = [3,4,4,4,4,5,5,5]


k = 3
res = Solution().sliding_window_maximum(nums4, k)
print(res)

if res == expected4:
    print("Success :)")
else:
    print("Failed :(")