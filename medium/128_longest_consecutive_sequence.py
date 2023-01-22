class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        seen = set()

        li = []
        for n in nums:
            if n not in seen:
                heapq.heappush(li,n)
                seen.add(n)

        count = 1
        maxCount = 1
        prev = heapq.heappop(li)
        while len(li):
            n = heapq.heappop(li)
            if n - prev == 1:
                count += 1
            else:
                maxCount = max(maxCount,count)
                count = 1
            prev = n

        return max(maxCount, count)


"""
Time: O(2n)
Space: O(2n)

Push each element to a heap O(n), restrict duplicates with a "seen" set. 
Then pop them one by one and look for longest consecutive sequence.
"""