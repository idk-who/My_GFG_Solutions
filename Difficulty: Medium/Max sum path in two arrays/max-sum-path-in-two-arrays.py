#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        p1 = p2 = 0
        su1 = su2 = 0
        n, m = len(arr1), len(arr2)
        ans = 0
        
        while p1<n and p2<m:
            if arr1[p1] < arr2[p2]:
                su1 += arr1[p1]
                p1 += 1
            elif arr2[p2] < arr1[p1]:
                su2 += arr2[p2]
                p2 += 1
            else:
                ans += max(su1, su2) + arr1[p1]
                p1 += 1
                p2 += 1
                su1, su2 = 0, 0
        while p1<n:
            su1 += arr1[p1]
            p1 += 1
        while p2<m:
            su2 += arr2[p2]
            p2 += 1
        ans += max(su1, su2)
        
        return ans


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)

# } Driver Code Ends