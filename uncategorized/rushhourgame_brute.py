from copy import deepcopy
from colorama import Fore
from random import shuffle

colors = {
    'red': Fore.RED,
    'a':Fore.MAGENTA,
    'b':Fore.YELLOW,
    'c':Fore.GREEN,
    'd':Fore.CYAN,
    'e':Fore.LIGHTBLUE_EX,
    'f':Fore.BLUE,
    'g':Fore.MAGENTA,
    'h':Fore.LIGHTCYAN_EX,
    'i':Fore.LIGHTGREEN_EX,
    'j':Fore.LIGHTRED_EX,
    'k':Fore.LIGHTMAGENTA_EX,
}


class RushHourSolution:
    def __init__(self, n, cars, useShuffle=True):
        self.n = 6
        self.exitRow = n // 2

        self.useShuffle = useShuffle

        self.cars = cars

        self.carsList = [i for i in self.cars.keys()]

        self.grid = [["." for i in range(self.n)] for j in range(self.n)]
        # add cars to grid
        for name, (f, b, dir) in self.cars.items():
            if dir == "h":
                for i in range(f[1], b[1] + 1):
                    self.grid[f[0]][i] = name
            else:
                for i in range(f[0], b[0] + 1):
                    self.grid[i][f[1]] = name


        # self.carsList = ['red']

        # # prio 1 verticals on exit path
        # for val in self.grid[self.exitRow]:
        #     if val != '.' and val != 'red':
        #         self.carsList.append(val)

        # # prio 2 stuff block first verticals
        # for row in range(self.n):
        #     for col in range(2,self.n):
        #         val = self.grid[row][col]
        #         if val != 'red' and val != '.' and val not in self.carsList:
        #             self.carsList.append(val)

        # # prio 3 verticals and horizonals blocking secondary
        # for row in range(self.n):
        #     for col in range(2):
        #         val = self.grid[row][col]
        #         if val != 'red' and val != '.' and val not in self.carsList:
        #             self.carsList.append(val)

        # carlist = [i for i in self.cars.keys()]
        # print(len(carlist), len(self.carsList))
        # print(self.carsList)
        


    def recursivelyFindExit(self, grid, carPositions, pastMoves, gridHistory):
        if carPositions['red'][1][1] == self.n-1:
            return (True, pastMoves, grid)

        remainingCars = deepcopy(self.carsList)

        lastCar = pastMoves[-1][0]

        if lastCar != 'dummy':
            remainingCars.remove(lastCar)

        carsOnExitRow = []
        for val in grid[self.exitRow]:
            if val != 'red' and val != '.' and val != lastCar:
                carsOnExitRow.append(val)
                remainingCars.remove(val)

        if self.useShuffle:
            shuffle(remainingCars)
            # shuffle(carsOnExitRow)

        remainingCars = carsOnExitRow + remainingCars
        

        for car in remainingCars:
            possibleMoves = self.getMoveOptions(grid, carPositions, car)
            for move in possibleMoves:
                newGrid = deepcopy(grid)
                newCarPositions = deepcopy(carPositions)

                self.moveCar(newGrid,newCarPositions,car,move)
                # print(f"recursion depth: {len(pastMoves)}")
                # self.printGrid(newGrid)

                # avoid max recursion depth
                if len(pastMoves) == 980:
                    return (False, [], [])

                if newGrid not in gridHistory:
                    res = self.recursivelyFindExit(newGrid, newCarPositions, pastMoves + [(car,move)], gridHistory + [grid])
                    if res[0]:
                        return res
                    
                # else:
                    # print(f"^ grid seen, grid saved: {len(gridHistory)}")
                    # print("==========================================")
                    # for g in gridHistory:
                    #     self.printGrid(g)

                    # print("==========================================")

            del possibleMoves

        del remainingCars

        return (False, [], [])
    
    def exhaustivelyFindExit(self, grid, carPositions, pastMoves, gridHistory):
        res = (False, [], [])

        if carPositions['red'][1][1] == self.n-1:
            return (True, pastMoves, grid)

        remainingCars = deepcopy(self.carsList)

        lastCar = pastMoves[-1][0]

        if lastCar != 'dummy':
            remainingCars.remove(lastCar)

        # shuffle(remainingCars)

        for car in remainingCars:
            possibleMoves = self.getMoveOptions(grid, carPositions, car)
            for move in possibleMoves:
                newGrid = deepcopy(grid)
                newCarPositions = deepcopy(carPositions)

                self.moveCar(newGrid,newCarPositions,car,move)
                # print(f"recursion depth: {len(pastMoves)}")

                # avoid max recursion depth
                if len(pastMoves) == 980:
                    return (False, [], [])

                if newGrid not in gridHistory:
                    currRes = self.exhaustivelyFindExit(newGrid, newCarPositions, pastMoves + [(car,move)], gridHistory + [grid])
                    if len(res[1]) == 0:
                        res = currRes
                    else:
                        if len(currRes[1]) < len(res[1]):
                            res = currRes

            del possibleMoves

        del remainingCars

        return res



    def getMoveOptions(self, grid, carPositions, carName):
        a, b, orientation = carPositions[carName]

        options = []

        if orientation == "h":
            # check right
            for i in range(b[1] + 1, self.n):
                if grid[b[0]][i] == ".":
                    options.append(i - b[1])
                else:
                    break
            # check left
            for i in range(a[1] - 1, -1, -1):
                if grid[a[0]][i] == ".":
                    options.append(i - a[1])
                else:
                    break
        else:
            # check down
            for i in range(b[0] + 1, self.n):
                if grid[i][b[1]] == ".":
                    options.append(i - b[0])
                else:
                    break
            # check ups
            for i in range(a[0] - 1, -1, -1):
                if grid[i][a[1]] == ".":
                    options.append(i - a[0])
                else:
                    break

        return options


    def moveCar(self, grid, carPositions, carName, steps):
        # print(f"moveCar: {colors[carName] + carName + Fore.WHITE}, steps: {steps}")

        a, b, orientation = carPositions[carName]
        if orientation == "h":
            # remove car from grid row
            for i in range(self.n):
                if grid[a[0]][i] == carName:
                    grid[a[0]][i] = "."

            a[1] += steps
            b[1] += steps

            # add new pos of car to grid
            for i in range(a[1], b[1] + 1):
                grid[a[0]][i] = carName
        else:
            # remove car from grid col
            for i in range(self.n):
                if grid[i][a[1]] == carName:
                    grid[i][a[1]] = "."

            a[0] += steps
            b[0] += steps

            # add new pos of car to grid
            for i in range(a[0], b[0] + 1):
                grid[i][a[1]] = carName

        currCarPos = (a, b, orientation)
        carPositions[carName] = currCarPos

        # self.gridHistoryStack.append(deepcopy(self.grid))

    def printGrid(self,grid):
        print("", end="\t")
        for i in range(self.n):
            print(Fore.WHITE + str(i), end="\t")

        print("\n")

        for i, row in enumerate(grid):
            print(Fore.WHITE + str(i), end="\t")
            for val in row:
                color = Fore.WHITE if val not in colors else colors[val]
                print(color + val, end="\t")
            if i == self.exitRow:
                print(Fore.WHITE + "<-- exit", end="")
            print("\n")

        print(Fore.WHITE + "-------------------------------------------------")


    def findExit(self):

        self.printGrid(self.grid)

        solExists, moves, finalGrid = self.recursivelyFindExit(self.grid, self.cars, [('dummy',1)], [deepcopy(self.grid)])
        # solExists, moves, finalGrid = self.exhaustivelyFindExit(self.grid, self.cars, [('dummy',1)], [deepcopy(self.grid)])

        if solExists:
            self.printGrid(finalGrid)
            print(f"number of moves: {len(moves)}")
        else:
            print("Solution doesnt exist, aka deadlock")

        return solExists, moves
    

# only moving red car forward
cars1 = {
    "red": ([3, 0], [3, 1], "h"),
    "a": ([0, 0], [0, 1], "h"),
    "b": ([3, 5], [5, 5], "v"),
    "c": ([2, 3], [3, 3], "v"),
    "d": ([1, 3], [1, 4], "h"),
    "e": ([5, 2], [5, 4], "h"),
    "f": ([2, 2], [3, 2], "v"),
}

# involves moving red car forward and backward
cars2 = {
    "red": ([3, 1], [3, 2], "h"),
    "a": ([4, 2], [5, 2], "v"),
    "b": ([4, 3], [4, 4], "h"),
    "c": ([3, 5], [4, 5], "v"),
    "d": ([5, 3], [5, 5], "h"),
    "e": ([2, 3], [3, 3], "v"),
    "f": ([2, 4], [3, 4], "v"),
    "g": ([1, 3], [1, 4], "h"),
    "h": ([0, 5], [2, 5], "v"),
    "k": ([0, 1], [2, 1], "v"),
}

# contain cycle
cars3 = {
    "red": ([3, 0], [3, 1], "h"),
    "a": ([0, 0], [1, 0], "v"),
    "b": ([0, 1], [0, 2], "h"),
    "c": ([1, 2], [2, 2], "v"),
    "d": ([2, 0], [2, 1], "h"),
    "e": ([3, 2], [4, 2], "v"),
    "f": ([0, 3], [2, 3], "v"),
    "g": ([3, 3], [4, 3], "v"),
    "h": ([5, 1], [5, 2], "h"),
    "i": ([0, 4], [2, 4], "v"),
    "k": ([0, 5], [2, 5], "v"),
    "m": ([4, 4], [5, 4], "v"),
    "n": ([4, 5], [5, 5], "v"),
}

minMoves = 999999
for i in range(1):

    # s1 = RushHourSolution(6, cars1, useShuffle=True)
    s1 = RushHourSolution(6, cars2, useShuffle=False)
    # s1 = RushHourSolution(6, cars3, useShuffle=False)

    solExists, moves = s1.findExit()
    if solExists:
        minMoves = min(minMoves,len(moves))

print(f"min moves: {minMoves}")


"""
if car reaches grid[exitRow][n-1] then it can exit

while redcarpos != at exit
    try to move it up,
    if ok then go,
    else:
        identify which piece is blocking and try to move it enough to give way for curr piece (NOT SIMPLY BY ONE SPACE)
        if blocked then find next piece trying to block it recursively or while loop until piece can move


        
        
        
if recursively got to the starting red block and red has no unblocking moves then return and go up tree
if 

a   b   b   f   i   k
a   .   c   f   i   k
d   d   c   f   i   k
red red e   g   .   . <- exit
.   .   e   g   m   n
.   h   h   .   m   n

!!! unblocking can be in a row like g shifting down to unblock f

!!! c-b-a-d-> cycle needs to be detected
"""
