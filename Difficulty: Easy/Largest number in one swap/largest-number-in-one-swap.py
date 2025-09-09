class Solution:
    def largestSwap(self, s):
        #code here
        aim = sorted(list(s), reverse=True)
        
        ans = list(s)
        
        for i in range(len(s)):
            if aim[i] != ans[i]:
                tar = aim[i]
                for j in range(len(s)-1, -1, -1):
                    if ans[j] == tar:
                        ans[i], ans[j] = ans[j], ans[i]
                        return "".join(ans)
        
        return s