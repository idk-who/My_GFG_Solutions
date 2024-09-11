from typing import List
from queue import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        traversal = []
        visited = [False]*V
        
        q = deque([0])
        visited[0] = True
        
        while q:
            u = q.popleft()
            traversal.append(u)
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        return traversal


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends