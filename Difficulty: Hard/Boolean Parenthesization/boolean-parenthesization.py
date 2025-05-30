#User function Template for python3
class Solution:
    def countWays(self, s):
        n = len(s)
        # code here
        from functools import lru_cache
        
        @lru_cache(None)
        def count(i, j, result=True):
            if i == j:
                if result:
                    return int(s[i:j+1] == 'T')
                else:
                    return int(s[i:j+1] == 'F')
            r = 0
            for k in range(i+1, j, 2):
                if s[k] == '&':
                    if result:
                        r += count(i, k-1, True) * count(k+1, j, True)
                    else:
                        r += count(i, k-1, False) * count(k+1, j, False)
                        r += count(i, k-1, False) * count(k+1, j, True)
                        r += count(i, k-1, True) * count(k+1, j, False)
                if s[k] == '|':
                    if result:
                        r += count(i, k-1, True) * count(k+1, j, False)
                        r += count(i, k-1, False) * count(k+1, j, True)
                        r += count(i, k-1, True) * count(k+1, j, True)
                    else:
                        r += count(i, k-1, False) * count(k+1, j, False)
                if s[k] == '^':
                    if result:
                        r += count(i, k-1, True) * count(k+1, j, False)
                        r += count(i, k-1, False) * count(k+1, j, True)
                    else:
                        r += count(i, k-1, False) * count(k+1, j, False)
                        r += count(i, k-1, True) * count(k+1, j, True)
            return r
        return count(0, n-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        print(Solution().countWays(s))
        print("~")

# } Driver Code Ends