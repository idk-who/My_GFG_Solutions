class Solution:
	def mergeOverlap(self, arr):
		arr.sort()
		ans = []
		start = arr[0][0]
		end = arr[0][1]
		for i in range(1, len(arr)):
		    if end >= arr[i][0]:
                end = max(end, arr[i][1])
            else:
                ans.append([start, end])
                start = arr[i][0]
                end = arr[i][1]
        ans.append([start, end])
		return ans


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()

# } Driver Code Ends