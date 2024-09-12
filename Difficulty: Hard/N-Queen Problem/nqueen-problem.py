#User function Template for python3

class Solution:
    def nQueen(self, n):
        board = [[False]*n for _ in range(n)]
        all_solutions = []
        
        def is_safe(board, i, j):
            dj = 0
            while i >= 0:
                if board[i][j]:
                    return False
                if j + dj < n and board[i][j+dj]:
                    return False
                if j - dj >= 0 and board[i][j-dj]:
                    return False
                dj += 1
                i -= 1
            return True
                
        
        def rec(board, i, soln = []):
            if i == n:
                all_solutions.append(soln[:])
                return
            for j in range(n):
                if is_safe(board, i, j):
                    board[i][j] = True
                    soln.append(j+1)
                    rec(board, i+1, soln)
                    soln.pop()
                    board[i][j] = False
        
        rec(board, 0, [])
    
        return all_solutions

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends