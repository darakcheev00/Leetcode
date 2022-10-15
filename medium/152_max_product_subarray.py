class Solution:
    def maxProduct(self, nums: List[int]) -> int:        
        
        maxP = nums[0]
        zeroFlag = False
        temp = []
        for ind, j in enumerate(nums):
            zeroFlag = j == 0 or zeroFlag
            
            if j != 0:
                temp.append(j)
            
            if (j == 0 and len(temp) != 0) or (ind == len(nums)-1):
                p1,p2 = 1,1
                for i in range(len(temp)):
                    p1 *= temp[i]
                    p2 *= temp[len(temp)-1-i]

                    if p1 > maxP:
                        maxP = p1

                    if p2 > maxP:
                        maxP = p2
                        
                temp = []                
                
        return max(maxP,0) if zeroFlag else maxP
    
"""
Time = O(n)
Space = O(n)

Idea: 
If the array contains no zeros then the max subarray will always start 
from the edges (odd or even length). In this case find a cumulative prod 
going forwards and backwards for each index. The max of these numbers will 
be the max subarray prod.
A zero will turn any subarray prod to 0 so if there are zeros in the array 
then split array into subarrays based on the zeros (accumulate nums into 
temp array until hit a 0). Then just process the temp array as described before.
Meanwhile update the max prod seen.
Return either the max prod seen or 0 if the array contained zeros because 
if the max prod is a negative then any temp array could absorb the zero and 
raise the value to 0.
If no zeros exist then just return max prod seen.
"""
            
            