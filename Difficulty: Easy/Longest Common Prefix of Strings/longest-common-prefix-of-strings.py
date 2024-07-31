#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        ptr = 0
        
        ml = len(min(arr))
        
        for i in range(ml):
            if all([arr[j][i]==arr[0][i] for j in range(1, len(arr))]):
                ptr += 1
            else:
                break
        
        return arr[0][:ptr] if ptr != 0 else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends