class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list=[[] for _ in range(numCourses)]
        indegrees=[0 for _ in range(numCourses)]
        for u,v in prerequisites:
            adj_list[v].append(u)
            indegrees[u]+=1
        queue = deque()
        result=[]
        for i in range(numCourses):
            if indegrees[i]==0:
                queue.append(i)
        while len(queue)!=0:
            curr_node=queue.popleft()
            result.append(curr_node)
            for adjNode in adj_list[curr_node]:
                indegrees[adjNode]-=1
                if indegrees[adjNode]==0:
                    queue.append(adjNode)
        if len(result)==numCourses:
            return result
        return []