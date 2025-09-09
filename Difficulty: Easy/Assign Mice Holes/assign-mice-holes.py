class Solution:
    def assignHole(self, mices, holes):
        mices.sort()
        holes.sort()
        
        ans = 0
        
        for i in range(len(mices)):
            ans = max(
                ans,
                abs(mices[i]-holes[i])
            )
        
        return ans