class Solution:
    def mergeArrays(self, a, b):
        p1 = len(a) - 1
        p2 = 0
        
        while p1 >= 0 and p2 < len(b):
            if a[p1] > b[p2]:
                a[p1], b[p2] = b[p2], a[p1]
                p1 -= 1
                p2 += 1
            else:
                break
        
        a.sort()
        b.sort()


#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends