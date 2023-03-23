class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        intervals.sort(key=lambda x: x[1])

        count = 0
        i = 0
        for j in range(1,len(intervals)):
            if intervals[i][1] > intervals[j][0]:
                count += 1
            else:
                i = j

        return count


"""
---- [1,11]
  ---- [2,12]
    ----- [11,22]
-------------------
"""

"""
Idea

Treat each interval as a stick (example below). You want to remove the minumum number of sticks so that none are left overlapping.
First sort the sticks based on the end.
Then loop and remove any stick that begins before the previous one ends. Count those occurences.
"""