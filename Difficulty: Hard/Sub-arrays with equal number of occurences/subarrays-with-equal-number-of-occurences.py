#User function Template for python3

class Solution:
    def sameOccurrence(self, arr, x, y):
        from collections import defaultdict
        cnt=defaultdict(int)
        cnt[0]=1
        pfs=0
        ret=0
        for ve in arr:
            pfs+=1 if ve==x else -1 if ve==y else 0
            ret+=cnt[pfs]
            cnt[pfs]+=1
        return ret

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        y = int(input().strip())
        ob = Solution()
        ans = ob.sameOccurrence(arr, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends