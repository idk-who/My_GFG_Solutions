class Solution:
    def checkSorted(self, arr):
        temp = 0
        for i in range(len(arr)):
            if arr[i] != i+1:
                if arr[arr[i]-1] == i + 1:
                    temp += 0.5
                else:
                    temp += 1
        
        # print(temp)
        return temp == 0 or temp == 2 or temp == 3
        


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends