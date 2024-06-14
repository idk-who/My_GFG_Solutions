#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        return "true" if sum(map(lambda x: int(x)**3, list(str(n)))) == n else "false"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends