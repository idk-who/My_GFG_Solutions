#User function Template for python3
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        flag=0
        for x in range(len(arr)-1):
            if arr[x] in arr[x+1:x+k+1]:
                flag=1
                break
        if flag==1:
            return True
        else:
            return False 

#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.checkDuplicatesWithinK(arr, k)
        if res:
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1
# } Driver Code Ends