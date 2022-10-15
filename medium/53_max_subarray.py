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