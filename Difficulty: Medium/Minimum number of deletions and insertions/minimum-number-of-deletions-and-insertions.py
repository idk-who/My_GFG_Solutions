#User function Template for python3
class Solution:
	def minOperations(self, str1, str2):
	    def lcs(s1, s2, p1, p2, d):
	        if p1 == len(s1) or p2 == len(s2):
	            return 0
	        
	        if (p1, p2) in d:
	            return d[(p1, p2)]
	        
	        if s1[p1] == s2[p2]:
	            ma = 1 + lcs(s1, s2, p1+1, p2+1, d)
	        else:
	            ma = max(
	                lcs(s1, s2, p1+1, p2, d),
	                lcs(s1, s2, p1, p2+1, d)
	                )
	        d[(p1, p2)] = ma
	        return ma
	   
        ls = lcs(str1, str2, 0, 0, dict())
	   
        return len(str1) - ls + len(str2) - ls


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s1, s2 = input().split()
        ob = Solution()
        ans = ob.minOperations(s1, s2)
        print(ans)

# } Driver Code Ends