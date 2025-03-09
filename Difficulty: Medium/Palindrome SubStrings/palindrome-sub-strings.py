#User function Template for python3

class Solution:

    def countPS(self, s):
        # code here
        n = len(s)
        cnt = 0
        
        for i in range(n):
            le = 1
            while i-le >= 0 and i+le < n:
                if s[i-le] == s[i+le]:
                    le += 1
                else:
                    break
            cnt += (le-1)
            
            le = 1
            while i-le >= 0 and i+le-1 < n:
                if s[i-le] == s[i+le-1]:
                    le += 1
                else:
                    break
            cnt += (le-1)
                
        return cnt

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.countPS(s))

        print("~")
# } Driver Code Ends