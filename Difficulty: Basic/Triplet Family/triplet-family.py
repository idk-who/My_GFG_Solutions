class Solution:
    def findTriplet(self, arr):
        if len(arr) < 3:
            return False
        arr.sort()
        
        for i in range(len(arr)):
            j = i + 1
            k = i + 2
            while j < len(arr) and k < len(arr):
                if arr[i] + arr[j] == arr[k] and j != k:
                    return True
                elif arr[i] + arr[j] < arr[k]:
                    j += 1
                else:
                    k += 1
        
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findTriplet(arr)
        if (res):
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1

# } Driver Code Ends