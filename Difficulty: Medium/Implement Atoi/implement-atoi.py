#User function template for Python
class Solution:
    def myAtoi(self, s):
        ans = 0
        ptr = 0
        while ptr < len(s) and s[ptr] == " ":
            ptr += 1
        neg = False
        if ptr < len(s) and s[ptr] == "-":
            neg = True
            ptr += 1
        while ptr < len(s) and s[ptr].isdigit():
            ans = ans*10 + int(s[ptr])
            ptr += 1
        
        if neg:
            ans = - ans
            
        if ans > 2**31 - 1:
            return 2**31 - 1
        if ans < -2**31:
            return -2**31
        return ans


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends