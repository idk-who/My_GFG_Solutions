class Solution:
    def isBridge(self, V, edges, c, d):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def rec(u, v):
            if u == v:
                return True
            visited.add(u)
            
            for u2 in adj[u]:
                if (u == c and u2 == d) or (u == d and u2 == c):
                    continue
                if u2 not in visited:
                    if rec(u2, v):
                        return True
            
            return False
        
        return not rec(c, d)
            



#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        adj = [[] for _ in range(V)]
        edges = []

        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
            edges.append([u, v])

        c = int(input())
        d = int(input())

        obj = Solution()
        l = obj.isBridge(V, edges, c, d)

        if l:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends