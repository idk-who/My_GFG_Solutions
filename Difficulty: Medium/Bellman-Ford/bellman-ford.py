#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, S):
        
        dist = [float('inf') for i in range(V)]
        dist[S] = 0
        for i in range(V-1):
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[v]>w+dist[u] :
                    dist[v] = min(dist[v], dist[u] + w)
                    
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return [-1]
                
        for i in range(len(dist)):
            if dist[i] == float('inf'):
                dist[i] = 100000000
        return dist

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V = int(input())
        E = int(input())
        edges = []
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            edges.append([u, v, w])
        S = int(input())
        ob = Solution()

        res = ob.bellmanFord(V, edges, S)
        for i in res:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends