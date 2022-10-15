class Solution:
    def findMin(self, nums: List[int]) -> int:
        # no rotation case
        if nums[0]<nums[-1]:
            return nums[0]
        
        return self.search(nums)
    
    def search(self, temp):
        l = len(temp)
        if l == 2:
            return min(temp[0],temp[1])
        elif l == 1:
            return temp[0]
        
        mid = len(temp)//2
        m = temp[mid]
        
        # checking if middle is the smallest
        if m < temp[mid-1]:
            return m
        
        if m > temp[-1]:
            # take right side
            return self.search(temp[mid+1:])
        else:
            # take left side
            return self.search(temp[:mid])
        
        
"""
Time: O(logn)
Space: O(1)

Idea:
Binary search but instead of checking if left or right is greater, check if middle is greater than the end value. Choose the right side if middle is greater than right end (meaning that array breaks/restarts on the right side). Else take left side.
"""
        
# notes:        
#     [2,3,4,5,6,7,8,9,1]
#     if middle is greater than end: take right
#               [7,8,9,1]
#                   [9,1]
    
#     [9,1,2,3,4,5,6,7,8]
#     else: take left
#     [9,1,2,3]
#     [9,1]
#     if len == 2:
#         max of [0],[1]
        
        