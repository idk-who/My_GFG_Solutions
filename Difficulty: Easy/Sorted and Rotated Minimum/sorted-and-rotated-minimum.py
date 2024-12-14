#User function Template for python3

class Solution:
    def findMin(self, arr):
        l = 0
        r = len(arr) - 1
        
        while l < r:
            if arr[l] < arr[r]:
                return arr[l]
                
            m = (l+r)//2
            if arr[m] < arr[l]:
                r = m
            else:
                l = m + 1
        
        return arr[l]

#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends