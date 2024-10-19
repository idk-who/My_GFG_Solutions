#User function Template for python3

class Solution:
    def roundToNearest (self, string) : 
        rem = string[-1]
        
        if rem <= '5':
            return string[:-1] + '0' 
        else:
            ans = list(string)
            ptr = len(ans) - 1
            ans[ptr] = '0'
            ptr -= 1
            while ptr >= 0 and ans[ptr] == '9':
                ans[ptr] = '0'
                ptr -= 1
            if ptr == -1:
                return '1' + "".join(ans)
            ans[ptr] = str(int(ans[ptr])+1)
            return "".join(ans)



#{ 
 # Driver Code Starts
#Initial Template for Python 3
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

# } Driver Code Ends