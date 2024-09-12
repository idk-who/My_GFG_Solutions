#User function Template for python3
from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        visited = [False]*V
        path = [False]*V
        
        
        def DFS(u, visited, path):
            visited[u] = True
                
            path[u] = True
            for v in adj[u]:
                if not visited[v]:
                    if DFS(v, visited, path):
                        return True
                elif path[v]:
                    return True
            path[u] = False
            
            return False

        for u in range(V):
            if not visited[u]:
                if DFS(u, visited, path):
                    return True
        return False
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)

# } Driver Code Ends