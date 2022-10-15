class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVol = 0
        a = 0
        b = len(height)-1
        
        while (a<b):
            ha, hb = height[a], height[b]
            maxVol = max((b-a)*min(ha,hb), maxVol)
                
            if ha < hb:
                a += 1
            else:
                b -= 1
        
        return maxVol

"""
Time = O(n)
Space = O(1)

Idea:
Use two pointers to narrow inwards updating max vol at each step.
Push the pointer of the shorter wall to try to max out water with other taller wall.
"""