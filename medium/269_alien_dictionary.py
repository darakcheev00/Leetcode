import collections

class Node(object):
    def __init__(self,val):
        self.val = val
        self.neighbors = []

    def connect(self, node):
        self.neighbors.append(node)

class Solution(object):
    def alienOrder(self,words):
        visited = set()

        def dfs(root,graph,visited):
            # 0 = not processed
            # in process
            visited[root] = 1
            for neighbor in graph[root].neighbors:
                if visited[neighbor.val] == 0:
                    if not dfs(neighbor.val,graph,visited):
                        return False
                elif visited[neighbor.val] == 1:
                    return False

            # finished processing
            visited[root] = 2
            self.ans += root
            return True

        self.ans = ""
        graph = {}
        #sets val to int=0 if key does not exist in dict
        visited = collections.defaultdict(int)
        self.topNum = 0

        for i in range(len(words)-1):
            # compare 2 words at a time
            a = words[i]
            b = words[i+1]
            # character index
            i = 0
            while i < len(a) and i < len(b):
                la = a[i]
                lb = b[i]

                # search for first letter that differs
                if la != lb:
                    print(la,lb)
                    # declare node pointers
                    nodeA = nobeB = None

                    # find nodes for letters in graph
                        # create Node if doesnt exist
                    if la not in graph:
                        nodeA = Node(la)
                        graph[la] = nodeA
                    else:
                        nodeA = graph[la]

                    if lb not in graph:
                        nodeB = Node(lb)
                        graph[lb] = nodeB
                    else:
                        nodeB = graph[lb]

                    # make dependency (la comes before lb)
                    nodeA.connect(nodeB)
                    
                    # only check the first letter that differs between the two words
                    break

                # move to next letter
                i += 1

            # if word a is longer than word b and no difference has been found then return 
            if i < len(a) and i >= len(b):
                print(a,b)
                return ""
            
        # for each unvisited letter in the graph run dfs to make connections
        for c in graph:
            if visited[c] == 0:
                if not dfs(c, graph, visited):
                    return ""

        # graph populated with connections at this point
        # print(graph)

        # make set containing all letters from words
        allLetters = set()
        for word in words:
            for c in word:
                allLetters.add(c)
        
        print(self.ans)

        for c in allLetters:
            # if letter doesnt have any order rules
            if c not in graph:
                self.ans += c

        return self.ans[::-1]


s1 = Solution()

words = [
    "wrt",
    "wrs",
    "wra",
    "wr"
    "wrf",
    "er",
    "ett",
    "rftt",
    "atf"
]
words = [
    "abe",
    "angle",
    "arcade",
    "art",
    "books",
    "butt",
    "buzz",
    "cent",
    "cifa"
    "cifal"
    "cifmqa"
]

print(words)
order = s1.alienOrder(words)
print(order)



        
""" My attempt """
# class Solution:
#     def findOrder(self, words):
#         graph = {}

#         # start graph
#         for i,w in enumerate(words):
#             words[i] = "."+w

#         # make graph
#         wordsNotFin = len(words)
#         while wordsNotFin > 0:
#             # get pairings
#             pairings = {}
#             for i,w in enumerate(words):
#                 if len(w)>1:
#                     main = w[0]
#                     sub = w[1]
#                     if main in pairings:
#                         pairings[main].append(sub)
#                         #rank = graph[main][-1][1] # last point in graph and adding one to rank
#                         #graph[main].append((sub,rank))
#                     else:
#                         pairings[main] = [sub]
#                 else:
#                     wordsNotFin -= 1

#                 #trim first letter
#                 words[i] = w[1:]

#             print(pairings)

#             # add to graph
#             for key in pairings:
#                 letters = pairings[key]
#                 if len(letters) <= 1:
#                     continue
#                 seen = set()
#                 graph[key] = []
#                 rank = 1
#                 for letter in letters:
#                     if letter not in seen and letter != key:
#                         graph[key].append((letter,rank))

#                         rank += 1
#                         seen.add(letter)  

#         print(f"graph: {graph}")

#         depths = {}

#         def dfs(n,cost,d):
#             if d in depths:
#                 depths[d].append(n)
#             else:
#                 depths[d] = [n]

#             if n in graph:
#                 for val,c in graph[n]:
#                     dfs(val,c,d+1)

#         dfs('.',0,0)

#         print(f"depths: {depths}")

#         res = ""
#         seen = set()
#         for i in range(len(depths)-1,0,-1):
#             arr = depths[i]
#             temp = ""
#             for j in arr:
#                 if j not in seen:
#                     temp += j
#                     seen.add(j)

#             res = temp + res

#         return res

# s1 = Solution()

# words = [
#     "wrt",
#     "wrs",
#     "wra",
#     "wrf",
#     "er",
#     "ett",
#     "rftt",
#     "atf"
# ]
# words = [
#     "abe",
#     "angle",
#     "arcade",
#     "art",
#     "books",
#     "butt",
#     "buzz",
#     "cent",
#     "cifa"
#     "cifmqa"
# ]

# print(words)
# order = s1.findOrder(words)
# print(order)

# # example graph

# graph = {
#     'a':[('b',1),('c',2),('d',3),('e',4)],
#     'b':[('d',1)],
#     'c':[('d',1),('f',2)],
#     'd':[('f',1),('e',2),('g',3)],
#     'e':[('g',1)],
#     'f':[('g',1)],
#     'g':[]
# }


