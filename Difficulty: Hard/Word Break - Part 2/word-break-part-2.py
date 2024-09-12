#User function Template for python3

class Solution:
    def wordBreak(self, cnt_words, words, s):
        n = len(s)
        dp = [None]*n
        mi = len(min(words, key = len))
        ma = len(max(words, key = len))
        words = set(words)
        
        def rec(s, i, dp):
            if i == n:
                return [""]
            
            all_poss = []
            for di in range(mi, min(ma, n)+1):
                if s[i:i+di] in words:
                    poss = rec(s, i+di, dp)
                    
                    for p in poss:
                        all_poss.append(
                            s[i:i+di]+(
                                (" "+p) if p != "" else p
                                )
                            )
            
            return all_poss
        
        ans = rec(s, 0, dp)
        
        return ans
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        dicti = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.wordBreak(n, dicti, s)
        if(len(ans) == 0):
            print("Empty")
        else:
            ans.sort()
            for it in (ans):
                print("("+it,end = ")")
            print()
# } Driver Code Ends