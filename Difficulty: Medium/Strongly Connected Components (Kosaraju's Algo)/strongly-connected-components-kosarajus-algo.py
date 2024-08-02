#User function Template for python3

class Solution:
    def kosaraju(self, V, adj):
        stack = []
        visited = [False]*V
        
        def DFS(adj, visited, u, st):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    DFS(adj, visited, v, st)    
            st.append(u)
        
        for u in range(V):
            if not visited[u]:
                DFS(adj, visited, u, stack)
        
        
        rg = [[] for _ in range(V)]
        for u in range(V):
            for v in adj[u]:
                rg[v].append(u)
        
        def DFS2(adj, visited, u):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    DFS2(adj, visited, v)
        
        visited = [False]*V
        cnt = 0
        while stack:
            u = stack.pop()
            if not visited[u]:
                cnt += 1
                DFS2(rg, visited, u)
        
        return cnt
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends