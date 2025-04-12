class Solution:
	def floodFill(self, image, sr, sc, newColor):
	    n, m = len(image), len(image[0])
		#Code here
        org_col = image[sr][sc]
        
        def rec(sr, sc, prev_col):
            if 0 <= sr < n and 0 <= sc < m and image[sr][sc] == prev_col and image[sr][sc]!= newColor:
                curr_col = image[sr][sc]
                image[sr][sc] = newColor
                rec(sr+1, sc, curr_col)
                rec(sr-1, sc, curr_col)
                rec(sr, sc+1, curr_col)
                rec(sr, sc-1, curr_col)
        
        rec(sr, sc, org_col)
        
        return image



#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)

T = int(input())  # Read number of test cases
for i in range(T):
    n = int(input())
    m = int(input())

    # Reading the image matrix
    image = []
    for _ in range(n):
        image.append(list(map(int, input().split())))

    # Read starting row, column, and new color
    sr = int(input())
    sc = int(input())
    newColor = int(input())

    # Create an instance of the Solution class and apply floodFill
    obj = Solution()
    ans = obj.floodFill(image, sr, sc, newColor)

    for row in ans:
        print(" ".join(map(str, row)))
    print("~")

# } Driver Code Ends