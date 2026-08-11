class Solution:
    #Time: O(V + E)
    #Space: O(V + E)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = {}

        adjList = {i: [] for i in range(numCourses)}

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
            preReqSatisfied = q.popleft()

            for course in adjList[preReqSatisfied]:
                    indegrees[course] -= 1 #As we have satisified one prereq, update indegree
                    if indegrees[course]==0:
                        q.append(course)
                        taken += 1
        
        return taken == numCourses
            




        