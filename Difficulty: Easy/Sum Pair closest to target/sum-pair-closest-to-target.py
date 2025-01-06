#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        arr.sort()
        
        diff = float("inf")
        ans = ()
        
        l = 0
        r = len(arr) - 1
        
        while l < r:
            d = arr[r] + arr[l]
            
            if abs(target - d) < diff:
                diff = abs(target - d)
                ans = (arr[l], arr[r])
            
            if d < target:
                l += 1
            else:
                r -= 1
                
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends