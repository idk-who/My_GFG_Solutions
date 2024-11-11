#User function Template for python3

class Solution:
    def minIncrements(self, arr):
        ans = 0
        arr.sort()
        prev = arr[0]
        for i in range(1, len(arr)):
            if prev >= arr[i]:
                ans += prev-arr[i] + 1
                prev += 1
            else:
                prev = arr[i]
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))

        T -= 1

# } Driver Code Ends