import heapq as hq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counts = {}

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 0

        for key in counts:
            hq.heappush(heap,(-1*counts[key],key))

        res = []
        for i in range(k):
            res.append(hq.heappop(heap)[1]) 
        return res



"""
Idea

First get counts of numbers.
Then add the pairs '(value, count)' to a heapn with a negative count cuz its a min heap.
Pop the top k to get the k most frequent.
"""