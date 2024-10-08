#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        d = {0:-1}
        ans = 0
        su = 0
        for ind, ele in enumerate(arr):
            su += ele
            
            if su in d:
                ans = max(ans, ind-d[su])
            else:
                d[su] = ind
                
        return ans


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends