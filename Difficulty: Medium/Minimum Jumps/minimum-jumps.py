#User function Template for python3
class Solution:
	def minJumps(self, arr):
	    jp_ln = arr[0]
	    mx_ln = 0
	    ans = 0
	    
	    for ptr in range(1, len(arr)):
            jp_ln -= 1
            mx_ln -= 1
            mx_ln = max(mx_ln, arr[ptr])
            
            if jp_ln < 0:
                return -1
            if jp_ln == 0:
                ans += 1
                jp_ln = mx_ln
                mx_ln = 0
        
        if mx_ln != 0: ans += 1
                
        return ans
        
        
	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)

# } Driver Code Ends