#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        
        l = 0
        r = 0
        su = 0
        
        while r < n:
            su += arr[r]
            
            while su > target:
                su -= arr[l]
                l += 1
            
            if su == target:
                return [l+1, r+1]
            
            r += 1
        
        return [-1]
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends