class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        n, m = len(mat), len(mat[0])
        ans = []
        left, up, right, down = 0, 0, m-1, n-1
        
        while left <= right and up <= down:
            for y in range(left, right+1):
                ans.append(mat[up][y])
            up += 1
            
            for x in range(up, down+1):
                ans.append(mat[x][right])
            right -= 1
            
            if up <= down:
                for y in range(right, left-1, -1):
                    ans.append(mat[down][y])
                down -= 1
            
            if left <= right:
                for x in range(down, up-1, -1):
                    ans.append(mat[x][left])
                left += 1
        
        return ans
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends