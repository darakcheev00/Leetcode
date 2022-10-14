# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        
        for i in range(len(nums)-1):
            res.append(nums[i]*res[-1])
            
        prod = 1
        for i in range(len(nums)-1,0,-1):
            prod *= nums[i]
            res[i-1] *= prod
            
        return res
        
# [1,2,3 , 4]
#  1,1,2,6       
# 24,12,8,6
    
    
        
        
            
            