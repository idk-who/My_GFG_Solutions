from collections import defaultdict
class Solution:
    def countTriplets(self, arr, target):
        sm1={}
        sm2={}
        ret=0
        for ve in arr:
            ret+=sm2.get(target-ve,0)
            for v in sm1:
                sm2[v+ve]=sm2.get(v+ve,0)+sm1.get(v,0)
            sm1[ve]=sm1.get(ve,0)+1
        return ret


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends