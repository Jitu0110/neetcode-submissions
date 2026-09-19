class Solution:
        def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
            prices = [float("inf")] * n
            prices[src] = 0
            
            #Time- O(E.K)
            #Space - O(N)
            for i in range(k+1):

                tmpPrices = prices.copy() #OR prices[:]

                for s,d,p in flights:
                    if prices[s] == float("inf"):
                        continue
                    
                    if prices[s] + p < tmpPrices[d]:
                        tmpPrices[d] = prices[s] + p 

                prices = tmpPrices

            return -1 if prices[dst] == float("inf") else prices[dst] 




#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         #Bellmond-Ford
#         #Can be used to find shortest distance
#         #Using additional constraint here (with 'k' stops)
#         #Time complexity - O(E.K)
#         #Very similar to BFS
#         #BF can also deal with 'negative' weights, just FYI


#         #MY initial wrong attempt. This wont work because BFS forces it to take more than k trips. 
#         #Example where it fails:
#         #n=4, flights=[[0,1,1],[0,2,100],[1,2,1],[2,3,1]], src=0, dst=3, k=1
# #         Level 0: process 0, so prices[1]=1, prices[2]=100, and q=[1,2]
# # Level 1: process 1 first, which sets prices[2]=2. Then process 2, which reads the already-updated prices[2]=2 and sets prices[3]=3.

# #WE NEED A TEMP ARRAY!

#         prices = [float("inf")] * n

#         prices[src] = 0

#         q = deque([src])

#         adjList = {i:[] for i in range(n)}

#         for flight in flights:
#             adjList[flight[0]].append([flight[1], flight[2]])
        
#         count = 0
#         while q and count <= k:

#             for _ in range(len(q)):
#                 node = q.popleft()

#                 # if node == dst:
#                 #     return prices[dst]

#                 for flight in adjList[node]:
#                     q.append(flight[0])
#                     prices[flight[0]] = min(prices[flight[0]], prices[node] + flight[1])


#             count+=1
        
#         return -1 if prices[dst] == float("inf") else prices[dst] 





