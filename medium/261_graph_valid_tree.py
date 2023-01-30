class Solution:
    def validateTree(self,n,edges):
        if len(edges) < n-1:
            return False

        checklist = {i for i in range(n)}

        # make hash
        graph = {}
        for a,b in edges:
            checklist.remove(a)
            checklist.remove(b)
            if a in graph:
                graph[a].add(b)
            else:
                graph[a] = {b}

        print(graph)
        
        print(checklist)

        return False


nodes = 5
edges = [[0,1], [0,2], [0,3], [1,4]]

s1 = Solution()
res = s1.validateTree(nodes,edges)
print(res)