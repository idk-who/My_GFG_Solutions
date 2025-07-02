class Solution:
    def totalElements(self, arr):
        freq={}
        ans=0
        left=0
        for right in range(len(arr)):
            freq[arr[right]]=freq.get(arr[right],0)+1
            if len(freq)>2:
                freq[arr[left]]-=1
                if freq[arr[left]]==0:
                    del freq[arr[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans