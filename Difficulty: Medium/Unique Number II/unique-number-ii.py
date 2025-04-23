#User function Template for python3

class Solution:
	def singleNum(self, arr):
		s = set()
		
		for i in arr:
		    if i in s:
		        s.remove(i)
		    else:
		        s.add(i)
	    
	    return sorted(list(s))



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNum(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends