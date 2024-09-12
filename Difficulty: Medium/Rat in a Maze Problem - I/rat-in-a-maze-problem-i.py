from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        n = len(m)
        all_paths = []
        visited = [[False]*n for _ in range(n)]
        directions = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]
        
        def rec(i, j, path):
            if i == n-1 and j == n-1:
                all_paths.append(path)
                return
            
            for di, dj, d in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < n:
                    if visited[ni][nj] == False and m[ni][nj] == 1:
                        visited[ni][nj] = True
                        rec(ni, nj, path+d)
                        visited[ni][nj] = False
        
        if m[0][0] == 1: 
            visited[0][0] = True
            rec(0, 0, "")
        
        return all_paths
                        



#{ 
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends