class Solution:
    def caseSort(self,s):
        n=len(s)
        lower,upper=[],[]
        for i in range(n):
            if s[i].islower():
                lower.append(s[i])
            else:
                upper.append(s[i])
        lower.sort()
        upper.sort()
        ans=[]
        l,u=0,0
        for i in range(n):
            if s[i].islower():
                ans.append(lower[l])
                l+=1
            else:
                ans.append(upper[u])
                u+=1
        return "".join(ans)