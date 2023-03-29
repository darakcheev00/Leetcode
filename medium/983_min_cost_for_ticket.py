class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}

        def dfs(i):
          if i == len(days):
            return 0
          if i in cache:
            return cache[i]
          
          cache[i] = float("inf")
          for d,c in zip([1,7,30],costs):
            j = i
            while j < len(days) and days[j] < days[i] + d:
              j += 1
            cache[i] = min(cache[i], c + dfs(j))
          return cache[i]
        
        return dfs(0)


"""
Idea
DFS on tree of options with caching. 
For each pass and cost find the next unsatisfiable day by while looping.
"""



# stupid solution that doesnt pass all test cases
import math

def printIntervals(meetings):
    print(meetings)
    for m in meetings:
        print(" "*m[0] + "_"*(m[1]-m[0]+1)+f"{m}")

class Solution_Old:
    def mincostTickets(self, days, costs):
        if len(days) == 1:
            return costs[0]

        n = len(days)
        total_cost=0

        # interval = (start, end, cost)
        intervals = []

        crossover_ab = math.ceil(costs[1]/costs[0])
        crossover_bc = math.ceil(costs[2]/costs[1])*7
        print(crossover_ab,crossover_bc)

        # find 30-day pass intervals
        self.get_interals(days,30,costs[2],crossover_bc,intervals)
        # find 7-day pass intervals
        self.get_interals(days,7,costs[1],crossover_ab,intervals)
        # add 1-day pass intervals
        for day in days:
            intervals.append((day,day,costs[0]))

        # remove overlapping intervals and calc cost
        intervals.sort(key = lambda x: x[0])
        total_cost = intervals[0][2]
        main = intervals[0]
        for curr in intervals[1:]:
            print(curr)
            if main[1] < curr[0]:
                main = curr
                total_cost += main[2]
            print(total_cost)

        printIntervals(intervals)
        print(total_cost)
        return total_cost
    
    def get_interals(self, days, pass_size, cost, crossover, intervals):
        # for i in days:
        #     print(f"{i}\t",end ='')
        # print('')
        # for i in range(len(days)):
        #     print(f"{i}\t",end ='')
        # print('\n')

        start, end = 0,-1
        for i,day in enumerate(days):
            end += 1
            print(end-start+1,days[start:end+1])
            if end - start + 1 >= crossover:
                if day - days[start] + 1 > pass_size:
                    if days[end-1] - days[start] + 1 <= pass_size:
                        print(f"added {days[start:end]}")
                        intervals.append((days[start],days[end-1],cost))

                elif day - days[start] + 1 == pass_size or i == len(days)-1:
                    intervals.append((days[start],days[end],cost))
                
                while day - days[start] + 1 >= pass_size:
                    start += 1

            # print(intervals)


# days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,40,41,42,43]

# days = [1,2,3,4,50,51,52,53,54,60,70,80,90]
days = [1,5,7,10]
costs = [2,7,15]

s1 = Solution_Old()
s1.mincostTickets(days,costs)

# ----------------------------------
# -  - ---            -
#   [                            ]
#   [     ]

# number of days when 7 day pass is better than 1 day: ceil(b/a): eg 7/2 = 3.5 -> 4*1= 4 or more days within 7 day frame
# number of days when 30 day pass is better that 7 day: ceil(c/b): eg 15/7=2.1 -> 3*7= 21 or more days within 30 day frame
# 1,2,40
# 2/1 = 2 or more days within 2 day frame
# 40/2 = 20 or more days within 40 day frame

