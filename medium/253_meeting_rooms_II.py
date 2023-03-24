def printlines(meetings):
    print(meetings)
    for m in meetings:
        print(" "*m[0] + "_"*(m[1]-m[0]))

def printheap(heap):
    print("")
    print(heap)
    while len(heap):
        m = hq.heappeep(heap)
        print(m, end = "")
    print("")

def sol1(meetings):
    if len(meetings) == 1:
        return 1
    
    meetings.sort(key=lambda x: x[1])
    
    printlines(meetings)

    max_count = 0
    for i in range(0,len(meetings)-1):
        count = 1
        for j in range(i+1, len(meetings)):
            if meetings[i][1]>meetings[j][0]:
                count += 1
        max_count = max(count, max_count)
    
    return max_count

import heapq as hq
def sol2(meetings):
    if len(meetings) == 1:
        return 1
    
    printlines(meetings)
    
    heap = []

    for meeting in meetings:
        hq.heappush(heap, (meeting[0],1))
        hq.heappush(heap, (meeting[1],0))

    max_count = 0
    count = 0
    while len(heap):
        i,type = hq.heappop(heap)
        if type == 1:
            count += 1
        else:
            count -= 1

        max_count = max(max_count, count)
        
    return max_count

meetings_1 = [[1,4],[6,10],[4,5],[6,20],[18,34]]
meetings_2 = [[1,50],[20,30]]
meetings_3 = [[1,2],[4,5]]
meetings_4 = [[1,50],[20,30],[25,45],[32,40]]
meetings_5 = [[1,50],[20,30],[25,45],[18,40]]
meetings_6 = [[15,50],[20,30],[25,45],[32,40],[10,20],[5,22]]
meetings_7 = [[10,12],[10,50],[20,30],[25,45],[32,40],[10,20],[5,22]]



# nlogn + n^2
# print(f"Number of rooms needed: {sol1(meetings_7)}")

# nlogn + n
print(f"Number of rooms needed: {sol2(meetings_7)}")
