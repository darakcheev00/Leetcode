def canCompleteCircuit(gas, cost):
    n = len(gas)

    stations = set([i for i in range(1,n)])
    
    si = 0
    while len(stations) > 0:

        tank = 0
        completedLoop = True

        for i in range(n):
            currIndex = (si + i) % n
            tank += gas[currIndex]

            if tank < cost[currIndex]:
                completedLoop = False
                si = currIndex + 1
                if si in stations:
                    stations.remove(si)
                else:
                    si = stations.pop()
                break

            tank -= cost[currIndex]
            
        if completedLoop:
            return si

    return -1

print(canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
print(canCompleteCircuit([5,1,2,3,4],[2,3,4,5,1]))
print(canCompleteCircuit([2,3,4],[3,4,3]))