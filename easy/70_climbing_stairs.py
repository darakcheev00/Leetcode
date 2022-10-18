class Solution:
    def climbStairs(self, n: int) -> int:
        self.seen = {}
        return self.climber(n-1)+self.climber(n-2)
    
    def climber(self, n):
        if n < 0:
            return 0
        
        if n == 0 or n == 1:
            return 1
        
        if n in self.seen:
            return self.seen[n]
        
        self.seen[n] = self.climber(n-1) + self.climber(n-2)
        
        return self.seen[n]
        
        
# Method 1
# --------------------------------------------------
#         self.seen = {}
#         return self.climber(n)
    
#     def climber(self, totStepsLeft):
#         if totStepsLeft >= 0 and totStepsLeft <= 2:
#             return totStepsLeft
         
#         a = 0
#         b = 0
#         case1 = totStepsLeft - 1
#         case2 = totStepsLeft - 2
        
#         if case1 in self.seen:
#             a = self.seen[case1]
#         else:
#             a = self.climber(case1)
#             self.seen[case1] = a
            
#         if case2 in self.seen:
#             b = self.seen[case2]
#         else:
#             b = self.climber(case2)
#             self.seen[case2] = b
            
            
#         return a + b
        

"""
Time: O(n*m)
Space: O(n)

Idea:
create a cache that holds calculated results for visited nodes. 
This way the value can just be searched up and not recalculated.
"""