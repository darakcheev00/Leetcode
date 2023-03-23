def printlines(meetings):
    print(meetings)
    for m in meetings:
        print(" "*m[0] + "_"*(m[1]-m[0]))

def sol(meetings):
    if len(meetings) == 1:
        return 1
    
    meetings.sort(key=lambda x: x[1])
    
    printlines(meetings)

    max_count = 0
    count = 0
    i = 0

    for j in range(1, len(meetings)):
        if meetings[i][1]>meetings[j][0]:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
            i = j

    max_count = max(count, max_count)
    
    return max_count + 1


meetings_1 = [[1,4],[6,10],[4,5],[6,20],[18,34]]
meetings_2 = [[1,50],[20,30]]
meetings_3 = [[1,2],[4,5]]
meetings_4 = [[1,50],[20,30],[25,45],[32,40]]
meetings_5 = [[1,50],[20,30],[25,45],[18,40]]
meetings_6 = [[15,50],[20,30],[25,45],[32,40],[10,20],[5,22]]

print(f"Number of rooms needed: {sol(meetings_6)}")
