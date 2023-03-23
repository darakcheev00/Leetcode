class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]

        if newInterval[0] < intervals[0][0]:
            intervals = [newInterval] + intervals
        else:
            index = 0
            # insert into the last valid spot
            for i in range(len(intervals)):
                if newInterval[0] > intervals[i][0]:
                    index = i
            intervals = intervals[:index+1] + [newInterval] + intervals[index+1:]

        # merge intervals
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= res[-1][1]:
                if curr[1] > res[-1][1]:
                    res[-1][1] = curr[1]
            else:
                res.append(curr)

        return res


"""
idea:
just add the new interval, sort based on start, and merge intervals
to remove the sort, manually with linear time insert the interval into the already sorted list of intervals
"""

        
