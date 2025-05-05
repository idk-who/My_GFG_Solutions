#{ 
 # Driver Code Starts

# } Driver Code Ends

#User function Template for python3
class Solution:
    def findTarget(self, arr, target):
        from bisect import bisect_left
        
        i = bisect_left(arr, target)
        for j in range(max(0, i - 2), min(len(arr), i + 3)):
            if arr[j] == target:
                return j
        return -1
        
        

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())  # Number of test cases

    for _ in range(t):
        arr = list(map(int, input().strip().split()))  # Read the array
        target = int(input().strip())  # Read the target

        sln = Solution()
        ans = sln.findTarget(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends