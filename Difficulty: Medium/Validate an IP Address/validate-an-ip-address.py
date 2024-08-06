#User function Template for python3
class Solution:
    def isValid(self, str):
        ip = str.split('.')
        return len(ip) == 4 and all(map(lambda x: len(x) > 0 and (len(x) == 1 or x[0]!='0' ) and 0 <= int(x) <= 255, ip))



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends