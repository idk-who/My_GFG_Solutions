# User function Template for Python3

class Solution:
    def maxLength(self, str):
        # code here
        
        stack, ans = [], 0
        m = {}
        for i, e in enumerate(str):
            if e == '(':
                stack.append(i)
            elif stack:
                j = stack.pop()
                length = i-j+1
                length += m.get(j-1, 0)
                m[i] = length
                ans = max(ans, length)

        return ans


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))

# } Driver Code Ends