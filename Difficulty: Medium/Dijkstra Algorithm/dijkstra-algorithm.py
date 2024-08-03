from heapq import heappop, heappush

class Solution:
    def dijkstra(self, V, adj, S):
        min_dist = [float("inf")]*V
        min_dist[S] = 0
        
        h = [(0, S)]
        
        while h:
            d, u = heappop(h)
            
            for v, nd in adj[u]:
                if d+nd < min_dist[v]:
                    min_dist[v] = d+nd
                    heappush(h, (d+nd, v))
        
        return min_dist
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends