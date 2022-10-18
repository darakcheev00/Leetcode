class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        # build lists
        nList = []
        pList = []
        numZeros = 0
        for i in nums:
            if i == 0:
                numZeros += 1
            elif i < 0:
                nList.append(i)
            else:
                pList.append(i)
        
        # convert sets to lists
        nSet = set(nList)
        pSet = set(pList)
        
        if numZeros >= 3:
            res.add(tuple([0,0,0]))
                
        for n in nSet:
            target = -1 * n
            compSet = set()
            for p in pList:
                if p == target and numZeros > 0:
                    res.add(tuple([n,0,p]))
                else:
                    if p in compSet:
                        res.add(tuple([n,-1*(n+p),p]))
                    else:
                        compSet.add(-1*(n+p))
                        
                        
        for p in pSet:
            target = -1 * p
            compSet = set()
            for n in nList:
                if n != target:
                    if n in compSet:
                        res.add(tuple([n,-1*(n+p),p]))
                    else:
                        compSet.add(-1*(n+p))
                        
        return res

"""
Time: O(n + n^2 + n^2)
Space: O(3n)

Idea:
Split nums into neg and pos lists and count number of zeros.
If number of zeros is 3 then add [0,0,0].
Convert neg and pos lists into sets to have a copy without dups.
For each num in negs set find either the complement (if a zero was originally found), or a pair of numbers complementing in the positive list -> gives [-,0,+] and [-,+,+] combos.
Do the same for the pos set to get the [-,-,+] combos.
Use a set to hold res to eliminate dups.
"""
        
        
                
            