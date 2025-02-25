#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends


class Solution:
    def getMaxArea(self,heights):
        stack = [0]
        heights.append(0)
        ans = 0
        for i in range(1, len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                idx = stack.pop()
                h = heights[idx]
                w = i - stack[-1] - 1 if stack else i
                ans = max(ans, h * w)
            stack.append(i)
        return ans


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getMaxArea(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends