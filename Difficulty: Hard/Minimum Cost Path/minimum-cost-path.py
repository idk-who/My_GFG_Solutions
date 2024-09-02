from heapq import heappop, heappush

class Solution:
	def minimumCostPath(self, grid):
	    n = len(grid)
        
        dist = [[float("inf")]*n for _ in range(n)]
        
        h = []
        h = [(grid[0][0], 0, 0)] # d, x, y
        dist[0][0] = grid[0][0]
        
        while h:
            d, x, y = heappop(h)
            
            if x == n-1 and y == n-1: return d
            
            for dx, dy in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n:
                    if d+grid[nx][ny] < dist[nx][ny]:
                        dist[nx][ny] = d+grid[nx][ny]
                        heappush(h, (dist[nx][ny], nx, ny))

        return dist[-1][-1]
        
#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.minimumCostPath(grid)
	print(ans)

# } Driver Code Ends