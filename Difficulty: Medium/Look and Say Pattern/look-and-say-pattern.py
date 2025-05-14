class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        t = "1"    
        
        for i in range(1,n):
            n = ""
            j = 0
            while j < len(t):
                c = 1
                while j + 1 < len(t) and t[j] == t[j+1]:
                    
                    j += 1
                    c += 1
                n += str(c) + t[j]
                j += 1
            t = n
        return t


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countAndSay(n))

        print("~")
# } Driver Code Ends