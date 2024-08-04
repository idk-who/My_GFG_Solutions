#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def bitManipulation(self, num, i):
        print(int(num & (1 << (i-1)) != 0), num | (1 << (i-1)), num & ~(1 << (i-1)))

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, i = list(map(int, input().split()))
        ob = Solution()
        ob.bitManipulation(n, i)
# } Driver Code Ends