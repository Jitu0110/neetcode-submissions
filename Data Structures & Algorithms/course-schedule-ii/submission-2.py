class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
       
        #Time - O(V)
        adjList = {i: [] for i in range(numCourses)}
        
        #Time - O(E)
        for x,y in prerequisites:
            adjList[y].append(x)

        indegrees = [0] * numCourses

        for x,y in prerequisites:
            indegrees[x] += 1
        
        q = deque()

        #Add courses with 0 indegrees to queue to process
        for index, value in enumerate(indegrees):
            if value == 0:
                q.append(index)
                result.append(index)
        
        while q:
            preReqSatisfied = q.popleft()

            for course in adjList[preReqSatisfied]:
                    indegrees[course] -= 1 #As we have satisified one prereq, update indegree
                    if indegrees[course]==0:
                        q.append(course)
                        result.append(course)
        
        return result if (len(result) == numCourses) else []
        