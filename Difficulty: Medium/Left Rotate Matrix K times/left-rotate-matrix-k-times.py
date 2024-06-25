class Solution:
    def rotateMatrix(self, k, mat):
        # code here
        n, m = len(mat), len(mat[0])
        
        k = k % m
        
        temp = [0]*m
        
        for i in range(n):
            ptr = k
            for j in range(m):
                temp[j] = mat[i][ptr%m]
                ptr += 1
                
            mat[i][:] = temp
        
        return mat



#{ 
 # Driver Code Starts
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split(" "))
        mat = []
        for i in range(n):
            mat.append(list(map(int, input().strip().split(" "))))
        ob = Solution()
        ans = ob.rotateMatrix(k, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()

# } Driver Code Ends