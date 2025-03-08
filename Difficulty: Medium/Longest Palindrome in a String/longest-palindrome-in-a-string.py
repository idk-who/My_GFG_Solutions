
class Solution:
    def longestPalindrome(self, s):
        # code here
        n = len(s)
        ma = 0
        ma_ids = (0, 0)
        
        for i in range(n):
            le = 1
            while i-le >= 0 and i+le < n:
                if s[i-le] == s[i+le]:
                    le += 1
                else:
                    break
            odd_le = 2*(le-1) + 1
            if odd_le > ma:
                ma = odd_le
                ma_ids = (i-le+1, i+le-1)
            
            le = 1
            while i-le >= 0 and i+le-1 < n:
                if s[i-le] == s[i+le-1]:
                    le += 1
                else:
                    break
            even_le = 2*(le-1)
            if even_le > ma:
                ma = even_le
                ma_ids = (i-le+1, i+le-1-1)
                
        return s[ma_ids[0]:ma_ids[1]+1]
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalindrome(S)

        print(ans)
        print("~")
# } Driver Code Ends