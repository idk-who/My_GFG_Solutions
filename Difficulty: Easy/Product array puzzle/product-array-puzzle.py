#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        
        pre = []
        mul = 1
        for i in range(n):
            pre.append(mul)
            mul *= nums[i]
        
        suf = []
        mul = 1
        for i in range(n-1, -1, -1):
            suf.append(mul)
            mul *= nums[i]
        suf.reverse()
        
        ans = []
        for i in range(n):
            ans.append(pre[i]*suf[i])
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends