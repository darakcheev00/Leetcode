class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            
            mid = (right-left)//2 + left
            if nums[mid] == target:
                return mid
            
            if nums[left]< nums[mid]:
                #break on right
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                #break on left
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1                    
        
        return -1
        
"""
Time: O(n)
Space: O(1)

Idea:
Do binary search.
On each step determine if break is on left or right of middle, and then find out if the target is on the side with the break or not.
"""