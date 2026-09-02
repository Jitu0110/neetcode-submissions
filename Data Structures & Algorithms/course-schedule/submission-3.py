class Solution:
    #Time: O(V + E)
    #Space: O(V + E)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = {i: [] for i in range(numCourses)}

        # adjList = {}
        # for i in range(numCourses):
        #     adjList[i]=[]

        for x,y in prerequisites:
            adjList[y].append(x)

        indegrees = [0] * numCourses
        taken = 0

        for x,y in prerequisites:
            indegrees[x] += 1
        
        q = deque()

        #Add courses with 0 indegrees to queue to process
        for index, value in enumerate(indegrees):
            if value == 0:
                q.append(index)
                taken += 1
        
        while q:
            courseTaken = q.popleft()

            for course in adjList[courseTaken]:
                    indegrees[course] -= 1 #As we have satisified one prereq, update indegree
                    if indegrees[course]==0:
                        q.append(course)
                        taken += 1
        
        return taken == numCourses
            

#DFS with cycle detection
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

#         adjList = {i: [] for i in range(numCourses)}

#         for course, prereq in prerequisites:
#             adjList[prereq].append(course)

#         # 0 = unvisited
#         # 1 = currently in DFS path
#         # 2 = completely processed
#         state = [0] * numCourses

#         def dfs(course):
#             # We found a node already in the current path
#             if state[course] == 1:
#                 return False

#             # Already completely processed
#             if state[course] == 2:
#                 return True

#             # Mark as currently exploring
#             state[course] = 1

#             for nextCourse in adjList[course]:
#                 if not dfs(nextCourse):
#                     return False

#             # Finished exploring this course
#             state[course] = 2

#             return True

#         for course in range(numCourses):
#             if not dfs(course):
#                 return False

#         return True


        