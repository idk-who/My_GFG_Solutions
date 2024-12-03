class Solution:
    def minChar(self, s):
        if s == reversed(s):
            return 0
        s = s + s[::-1]
        lps = [0] * len(s)
        prev_lps = 0
        ptr = 1
        
        while ptr < len(s):
            if s[ptr] == s[prev_lps]:
                lps[ptr] = prev_lps + 1
                ptr += 1
                prev_lps += 1
            elif prev_lps == 0:
                ptr += 1
            else:
                prev_lps = lps[prev_lps-1]
        
        return len(s)//2 - lps[-1] 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends