#User function Template for python3
class Solution:
    def findMaximum(self, arr):
        # code here
        n = len(arr)
        
        l, r = 0, n-2
        
        while l<=r:
            mid=(l+r)//2
            
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return arr[mid]
                
            if arr[mid+1] > arr[mid]:
                l=mid+1
                
            else:
                r=mid-1
            
        
        return max(arr[n-1], arr[0])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends