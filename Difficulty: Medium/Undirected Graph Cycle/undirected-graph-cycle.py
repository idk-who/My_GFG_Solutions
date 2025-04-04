
class Solution:
	def isCycle(self, V, edges):
        
        adj = [[] for _ in range(V)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
		visited = set()
        def rec(u):
            visited.add(u)
            for v in adj[u]:
                if v in visited:
                    return True
                else:
                    if rec(v):
                        return True
            return False
        
        for i in range(V):
            if i not in visited:
                if rec(i):
                    return True
        
        return False

#{ 
 # Driver Code Starts
import sys
#Position this line where user code will be pasted.


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))

        obj = Solution()
        ans = obj.isCycle(V, edges)
        print("true" if ans else "false")
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends