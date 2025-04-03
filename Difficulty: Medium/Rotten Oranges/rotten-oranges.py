from collections import deque
class Solution:
	def orangesRotting(self, mat):
	    n, m = len(mat), len(mat[0])
        q = deque([])
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    q.append((i, j))
        
        def infect(i, j, t):
            if (not (0 <= i < n)) or (not (0 <= j < m)):
                return False
            if mat[i][j] != 1:
                return False
            mat[i][j] = t
            q.append((i, j))
        
        while q:
            i, j = q.popleft()
            
            next_t = mat[i][j] + 1
            
            infect(i-1, j, next_t)
            infect(i+1, j, next_t)
            infect(i, j-1, next_t)
            infect(i, j+1, next_t)
            # print(q)
        
        
        ans = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    return -1
                ans = max(ans, mat[i][j])
        
        if ans <= 2:
            return 0
        
        return ans - 2
        
        
        


#{ 
 # Driver Code Starts
from queue import Queue

T = int(input())
for i in range(T):
    n = int(input())
    m = int(input())
    mat = []
    for _ in range(n):
        a = list(map(int, input().split()))
        mat.append(a)
    obj = Solution()
    ans = obj.orangesRotting(mat)
    print(ans)
    print("~")

# } Driver Code Ends