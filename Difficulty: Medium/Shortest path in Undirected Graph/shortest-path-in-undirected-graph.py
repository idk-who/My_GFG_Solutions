from collections import deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        dist = [float("inf")]*n
        dist[src] = 0
        
        q = deque([(src, 0)])
        
        while q:
            u, d = q.popleft()
            
            for v in adj[u]:
                if d + 1 < dist[v]:
                    dist[v] = d+1
                    q.append((v, d+1))
        
        for i in range(n):
            if dist[i] == float("inf"):
                dist[i] = -1
        
        return dist


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends