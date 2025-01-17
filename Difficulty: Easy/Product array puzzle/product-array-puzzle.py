#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        prod = 1
        zeros = 0
        for i in arr:
            if i == 0:
                zeros += 1
            else:
                prod *= i
                
        if zeros > 1:
            return [0]*len(arr)
        
        ans = []
        
        for i in arr:
            if zeros:
                if i == 0:
                    ans.append(prod)
                else:
                    ans.append(0)
            else:
                ans.append(prod//i)
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends