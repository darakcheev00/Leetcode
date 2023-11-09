from copy import deepcopy
arr = [1,2,3]

def getPerms(nums):
    res = []

    if len(nums) == 1:
        return [nums]

    for i, val in enumerate(nums):
        copy = deepcopy(nums)
        copy.pop(i)
        subResults = getPerms(copy)
        for s in subResults:
            res.append([val] + s)

    return res


res = getPerms(arr)

for row in res:
    print(row)

print("")
res = getPerms([1,2,2])

for row in res:
    print(row)


"""
[1, 2, 3, 4] rot last 2 x1
[1, 2, 4, 3] rot last 3 x1
[1, 3, 2, 4] rot last 2 x1
[1, 3, 4, 2] rot last 3 x2 3 is greater than 1 and less than 1 of the ones to the right
[1, 4, 2, 3] rot last 2 x1
[1, 4, 3, 2] if all increasing from right except last (left most) then take next first (from sorted list) and sort the remaining
[2, 1, 3, 4] rot last 2 x1
[2, 1, 4, 3] rot last 3 x1
[2, 3, 1, 4] rot last 2 x1
[2, 3, 4, 1] rot last 3 x2  3 is greater than 1 and less than 1 of the ones to the right
[2, 4, 1, 3] rot last 2 x1
[2, 4, 3, 1] rot last 4 x2  2 is less than 2 and greater than 1 on the right
[3, 1, 2, 4] rot last 2 x1
[3, 1, 4, 2] rot last 3 x1
[3, 2, 1, 4] rot last 2 x1
[3, 2, 4, 1] rot last 3 x2  2 is greater than 1 on the right
[3, 4, 1, 2] rot last 2 x1
[3, 4, 2, 1] if all increasing from right except last (left most) then take next first (from sorted list) and sort the remaining
[4, 1, 2, 3] 
[4, 1, 3, 2] 
[4, 2, 1, 3] 
[4, 2, 3, 1] 
[4, 3, 1, 2] 
[4, 3, 2, 1] 


find first one that drops down one. keep left side. bump the current one to next available. sort the remaining ones from least to greatest and attach


"""