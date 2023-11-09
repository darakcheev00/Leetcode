from copy import deepcopy
from colorama import Fore

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
    def __init__(self, n, cars, redFront):
        self.n = 6
        self.exitRow = n // 2
        self.cars = cars
        self.red = ([self.exitRow, redFront - 1], [self.exitRow, redFront], "h")
        self.grid = [["." for i in range(self.n)] for j in range(self.n)]

        # red
        self.grid[self.red[0][0]][self.red[0][1]] = "red"
        self.grid[self.red[1][0]][self.red[1][1]] = "red"

        # other
        for name, (f, b, dir) in self.cars.items():
            if dir == "h":
                for i in range(f[1], b[1] + 1):
                    self.grid[f[0]][i] = name
            else:
                for i in range(f[0], b[0] + 1):
                    self.grid[i][f[1]] = name

        self.gridHistoryStack = [deepcopy(self.grid)]

    def findExit(self):
        self.printGrid()
        res = []

        while True:
            # find options of moves that red car can make
            redOptions = self.getRedMoveOptions()
            print(f"red Options: {redOptions}")

            # move red car forward
            foundMove = False
            rightOfRed = self.getNextCell("red", 1)
            if rightOfRed == "dne":
                # at right edge therefore can exit
                return res
            elif rightOfRed == ".":
                self.moveCar("red", 1, 1)
                foundMove = True
            else:
                print(f"red blocked by {rightOfRed}")

                blockingCar = rightOfRed

                # create list of options for the blocking car

                # TODO: filter options which actually unblock blocked car
                blockingCarOptions = self.getUnblockingMoveOptions(blockingCar)
                print(f"blocking car options to unblock: {blockingCarOptions}")

                if len(blockingCarOptions) == 0:
                    # no unblocking options therefore blocked itself
                    # find car which is block this car
                    # recursive call here maybe
                    break  # TEMP

                for option in blockingCarOptions:
                    # take move
                    self.moveCar(blockingCar, option)

                    # some further logic
                    # for next car

                    # undo move
                    self.moveCar(blockingCar, option * -1)

                if foundMove:
                    self.moveCar("red", 1, 1)

            # else move red car backward
            if not foundMove:
                leftOfRed = self.getNextCell("red", -1)
                print(f"leftOfRed: {leftOfRed}")

            break

        self.printGrid()

        return res

    def getUnblockingMoveOptions(self, carName):
        currCar = self.red if carName == "red" else self.cars[carName]
        a, b, orientation = currCar

        options = []

        if orientation == "h":
            # check right
            for i in range(b[1] + 1, self.n):
                if self.grid[b[0]][i] == ".":
                    options.append(i - b[1])
                else:
                    break
            # check left
            for i in range(a[1] - 1, -1, -1):
                if self.grid[a[0]][i] == ".":
                    options.append(i - a[1])
                else:
                    break
        else:
            # check down
            for i in range(b[0] + 1, self.n):
                if self.grid[i][b[1]] == ".":
                    options.append(i - b[0])
                else:
                    break
            # check ups
            for i in range(a[0] - 1, -1, -1):
                if self.grid[i][a[1]] == ".":
                    options.append(i - a[0])
                else:
                    break

        return options

    def getRedMoveOptions(self):
        a, b, _ = self.red
        options = []

        # check right
        for i in range(b[1] + 1, self.n):
            if self.grid[b[0]][i] == ".":
                options.append(i - b[1])
            else:
                break
        # check left
        for i in range(a[1] - 1, -1, -1):
            if self.grid[a[0]][i] == ".":
                options.append(i - a[1])
            else:
                break

        return options

    def getNextCell(self, carName, dir):
        currCar = self.red if carName == "red" else self.cars[carName]
        a, b, orientation = currCar

        if dir > 0:
            if orientation == "h":
                # right
                return "dne" if b[1] + 1 == self.n else self.grid[b[0]][b[1] + 1]
            else:
                # down
                return "dne" if b[0] + 1 == self.n else self.grid[b[0] + 1][b[1]]

        else:
            if orientation == "h":
                # left
                return "dne" if a[1] - 1 == -1 else self.grid[a[0]][a[1] - 1]
            else:
                # up
                return "dne" if a[0] - 1 == -1 else self.grid[a[0] - 1][a[1]]

    def moveCar(self, carName, steps):
        print(f"moveCar: {carName}, steps: {steps}")
        a, b, orientation = self.red if carName == "red" else self.cars[carName]
        if orientation == "h":
            # remove car from grid row
            for i in range(self.n):
                if self.grid[a[0]][i] == carName:
                    self.grid[a[0]][i] = "."

            a[1] += steps
            b[1] += steps

            # add new pos of car to grid
            for i in range(a[1], b[1] + 1):
                self.grid[a[0]][i] = carName
        else:
            # remove car from grid col
            for i in range(self.n):
                if self.grid[i][a[1]] == carName:
                    self.grid[i][a[1]] = "."

            a[0] += steps
            b[0] += steps

            # add new pos of car to grid
            for i in range(a[0], b[0] + 1):
                self.grid[i][a[1]] = carName

        currCarPos = (a, b, orientation)
        self.cars[carName] = currCarPos

        self.gridHistoryStack.append(deepcopy(self.grid))

    def printGrid(self):
        print("", end="\t")
        for i in range(self.n):
            print(Fore.WHITE + str(i), end="\t")

        print("\n")

        for i, row in enumerate(self.grid):
            print(Fore.WHITE + str(i), end="\t")
            for val in row:
                color = Fore.WHITE if val not in colors else colors[val]
                print(color + val, end="\t")
            if i == self.exitRow:
                print(Fore.WHITE + "<-- exit", end="")
            print("\n")

        print(Fore.WHITE + "-------------------------------------------------")


# only moving red car forward
cars1 = {
    "a": ([0, 0], [0, 1], "h"),
    "b": ([3, 5], [5, 5], "v"),
    "c": ([2, 3], [3, 3], "v"),
    "d": ([1, 3], [1, 4], "h"),
    "e": ([5, 2], [5, 4], "h"),
    "f": ([2, 2], [3, 2], "v"),
}

# involves moving red car forward and backward
cars2 = {
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

# s1 = RushHourSolution(6, cars1, 1)
# s1 = RushHourSolution(6, cars2, 2)
s1 = RushHourSolution(6, cars3, 1)
res = s1.findExit()
# print(res)

ans1 = [("red", "right", 1), ("d", "left", 2), ("c", "up", 1), ("b", "up", 3)]
# print(res == ans1)


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
