class Solution:
    def wordBreak(self, s, dictionary):
        di = set(dictionary)
        mi, ma = float('inf'), float('-inf')
        for i in dictionary:
            mi = min(mi, len(i))
            ma = max(ma, len(i))
        dp = [-1]*len(s)
        
        def rec(p1):
            if p1 == len(s):
                return True
            
            if dp[p1] != -1:
                return dp[p1]
            
            poss = False
            for p2 in range(p1+mi, min(len(s), p1+ma)+1):
                if s[p1:p2] in di:
                    if rec(p2):
                        poss = True
                        break
            dp[p1] = poss
            return poss
        
        return rec(0)


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        s = input().strip()
        dictionary = input().strip().split()
        ob = Solution()
        res = ob.wordBreak(s, dictionary)
        if res:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends