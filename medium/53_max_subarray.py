class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        
        currSum = 0
        for n in nums:
            currSum += n
            
            if currSum < 0:
                if n > maxSum:
                    maxSum = n
                currSum = 0             
            else:
                if currSum > maxSum:
                    maxSum = currSum
        
        return maxSum                

"""
Time = O(n)
Space = O(1)

Idea:
Iterate over nums accumulating a sum.
If the sum is negative at a step that means that the current running sum should
be reset to zero.
At each step the maxSum seen is updated accordingly.
"""