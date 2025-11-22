class Solution:
    def minConnect(self, V, edges):
        if V - 1 > len(edges):
            return -1
        
        adj = [[] for i in range(V)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        
        def mark_vis(i):
            vis[i] = True
            for v in adj[i]:
                if not vis[v]:
                    mark_vis(v)
        
        vis = [False]*V
        
        ans = -1
        for i in range(V):
            if not vis[i]:
                ans += 1
                mark_vis(i)
        
        return ans
