class Solution:
    def maxValue(self, arr):
        # skip first
        one, two = 0, arr[1]
        for i in range(2, len(arr)):
            one, two = two, max(two, arr[i]+one)
        ans = two
        
        # skip last
        one, two = 0, arr[0]
        for i in range(1, len(arr)-1):
            one, two = two, max(two, arr[i]+one)
        ans = max(ans, two)
        
        return ans



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends