def sol(meetings):
    

    if len(meetings)==1:
        return True

    meetings.sort(key = lambda x: x[0])

    i = 0
    for j in range(1,len(meetings)):
        if meetings[i][1] > meetings[j][0]:
            return False
        else:
            i = j
    return True

meetings_bad1 = [[1,3],[6,10],[4,5],[6,20],[18,34]]
meetings_bad2 = [[1,50],[20,30]]
meetings_good = [[1,2],[4,5]]
print(sol(meetings_bad2))