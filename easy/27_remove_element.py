# 27 remove element

class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
        front = 0
        back = len(nums)-1
        while front <= back:
            f,b = nums[front], nums[back]
            
            if f == val and b != val:
                temp = f
                nums[front] = b
                nums[back] = temp
                front += 1
            elif b == val:
                back -= 1
            elif f != val and b != val:
                front += 1
        
        return back+1, nums


print(Solution())
