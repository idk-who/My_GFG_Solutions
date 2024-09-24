from collections import Counter

class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        d = Counter(p)
        
        ans = ""
        
        l = 0
        n = len(s)
        for r in range(n):
            if s[r] in d:
                d[s[r]] -= 1
                
                all_found = True
                for k, v in d.items():
                    if v > 0:
                        all_found = False
                        break
                
                if all_found:
                    # print(l, r, d)
                    while l < n and (s[l] not in d or d[s[l]] < 0):
                        if s[l] in d:
                            d[s[l]] += 1
                        l += 1
                    if ans == "" or r+1-l < len(ans):
                        ans = s[l:r+1]
                        
                    d[s[l]] += 1
                    l += 1
                    # print(l, r, d, '\n')
                    
        return ans if ans != "" else -1
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends