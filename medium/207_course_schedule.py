class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adjacency list
        adjList = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            adjList[p].append(c)

        state = [0]*numCourses
        def hasCycle(course):
            if state[course] == 1:
                # this course has been processes so we pass
                return False
            
            if state[course] == -1:
                # is being processed, therefore in path, therefore cycle found
                return True

            state[course] = -1

            for v in adjList[course]:
                if hasCycle(v):
                    return True

            state[course] = 1
            return False # no cycle found

        for course in range(numCourses):
            if hasCycle(course):
                return False

        return True




        ## Solution 1
        def sol1():
            checked = [0]*numCourses

            # convert to map
            mapping = {}
            for c in prerequisites:
                thisCourse = c[0]
                if thisCourse in mapping:
                    mapping[thisCourse].append(c[1])
                else:
                    mapping[thisCourse] = [c[1]]

            def check(course,visited):
                if course not in mapping:
                    # this course does not have prereq's so pass
                    return True
                
                if course in visited:
                    # this course has been visited therefore cycle -> return false
                    return False

                for p in mapping[course]:
                    if checked[p] == 0:
                        newset = visited.union({course})
                        if not check(p,newset):
                            return False
                
                checked[course] = 1
                return True

            # populate all other courses with no prerequisites
            for index,state in enumerate(checked):
                if state == 0:
                    if not check(index,set()):
                        return False

            return True

"""
Make an adjacency table for all prerequisites. Course p is a prerequisite to these courses [x,y,z,....].
Loop through all courses and check if they have cycles using helper function:
Helper function:
    Runs dfs with memoization on the course graph.
    State of all courses is kept in an array:   
        0: init states: unvisited
        -1: currently processing (in the current search path)
        1: already checked = not cycle under this path, therefore dont need to check it

    if 1 then return false because course def does not have cycle]
    if -1 that means that this course is still being processed meaning its in the current path, 
        meaning that its in a cycle-> return true;
        
    Then set state of current course to processing and recursively check all dependencies.
    If any dependency check finds a cycle then just return false -> this will return out of the helper function.
"""  