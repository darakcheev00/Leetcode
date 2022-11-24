class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        # sort intervals based on start
        intervals.sort(key=lambda x: x[1])

        end = float('-inf')
        count = 0
        for i in intervals:
            s,e = i[0],i[1]
            if s >= end:
                end = e
            else:
                count +=1 
        
        return count
"""
Idea

Treat each interval as a stick (example below). You want to remove the minumum number of sticks so that none are left overlapping.
First sort the sticks based on the end.
Then loop and remove any stick that begins before the previous one ends. Count those occurences.
"""


# -------------------
#     ----------------- yes
#   ---------------------- yes
#             ------------------- yes
#                                        ------------------
#                                                                   ----------------
#                                                                              --------- yes


# --
#  --
# ---
#   --
