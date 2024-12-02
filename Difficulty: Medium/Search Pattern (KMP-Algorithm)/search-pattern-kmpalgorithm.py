#User function Template for python3

class Solution:
    def search(self, pat, txt):
        haystack = txt
        needle = pat
        
        lps = [0]*len(needle)
        
        prev_lps, ptr = 0, 1
        
        while ptr < len(needle):
            if needle[ptr] == needle[prev_lps]:
                lps[ptr] = prev_lps + 1
                ptr += 1
                prev_lps += 1
            elif prev_lps == 0:
                lps[ptr] = 0
                ptr += 1
            else:
                prev_lps = lps[prev_lps-1]
        
        
        i, j = 0, 0
        ans = []
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j-1]
            if j == len(needle):
                ans.append(i-j)
                j = lps[j-1]
                
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends