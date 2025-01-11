#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        inds = [-1]*26
        
        l = -1
        ans = 0
        for r, c in enumerate(s):
            if inds[ord(c)-ord('a')] >= l:
                l = inds[ord(c)-ord('a')] 
            inds[ord(c)-ord('a')] = r
            ans = max(ans, r-l)
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends