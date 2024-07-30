from heapq import heappush, heappop

class Solution:
	def minimumCostPath(self, grid):
		n, m = len(grid), len(grid[0])
		
		dist = [[float("inf")]*m for _ in range(n)]
		dist[0][0] = grid[0][0]
		
		h = [(dist[0][0], 0, 0)]
		
		while h:
		    d, i, j = heappop(h)
		    
		    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
		        ni, nj = i+di, j+dj
		        
		        if 0 <= ni < n and 0 <= nj < m:
		            if d + grid[ni][nj] < dist[ni][nj]:
		                dist[ni][nj] = d + grid[ni][nj]
		                heappush(h, (d + grid[ni][nj], ni, nj))
	    
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