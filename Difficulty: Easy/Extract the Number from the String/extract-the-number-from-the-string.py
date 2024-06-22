class Solution:
    def ExtractNumber(self,sentence):
        for i in sorted(sentence.split(), key = lambda x: (len(x), x), reverse=True):
            if i.isnumeric() and '9' not in i:
                return i
        
        return -1


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends