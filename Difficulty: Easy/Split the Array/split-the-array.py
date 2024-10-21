#User function Template for python3
class Solution:
	def countgroup(self,arr): 
        xor = 0
        for i in arr: xor ^= i
        
        if xor == 0:
            return pow(2, len(arr)-1, 10**9+7) - 1
        else:
            return 0



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countgroup(arr)
        print(res)
        t -= 1

# } Driver Code Ends