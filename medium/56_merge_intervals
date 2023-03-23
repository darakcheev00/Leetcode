class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
                
        intervals.sort(key= lambda x : x[0])
        res.append(intervals[0])
        
        for i in range(1,len(intervals)):
            curr = intervals[i]
            if curr[0] <= res[-1][1]:
                if curr[1] > res[-1][1]:
                    res[-1][1] = curr[1]
            else:
                res.append(curr)
        
        return res


"""
idea:
sort intervals based on start
add the first interval to the res list
for each of the other intervals check if the start overlaps with the ending of the last interval in res
    check if the current interval's end hangs off the edge of the last one in res
        if so then modify the ending of the last interval in res
if no overlap then just append interval to end of res
"""