# your task is to complete this function
# function should return True/False or 1/0
# str1: pattern
# str2: text
class Solution:
    def wildCard(self,pattern, string):
        def rec(p1, p2, dp):
            if p1 == len(pattern) and p2 == len(string):
                return True
            if p1 == len(pattern) and p2 < len(string):
                return False
            if p1 < len(pattern) and p2 == len(string):
                if pattern[p1] == '*':
                    return rec(p1+1, p2, dp)
                return False
            
            if (p1, p2) in dp:
                return dp[(p1, p2)]
            
            ma = False
            if pattern[p1] == '?':
                ma = rec(p1+1, p2+1, dp)
            elif pattern[p1] == '*':
                ma = (
                    rec(p1+1, p2, dp)
                    or
                    rec(p1, p2+1, dp)
                    or
                    rec(p1+1, p2+1, dp)
                    )
            else:
                ma = (
                    (pattern[p1] == string[p2])
                    and
                    rec(p1+1, p2+1, dp)
                    )
            
            dp[(p1, p2)] = ma
            
            return ma
        
        return rec(0, 0, dict())
            



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)

# } Driver Code Ends