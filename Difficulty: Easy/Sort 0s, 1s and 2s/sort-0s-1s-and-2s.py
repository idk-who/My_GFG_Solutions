#{ 
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        zero, one, two = 0, 0, 0
        for i in arr:
            if i == 0:
                zero += 1
            elif i == 1:
                one += 1
            else:
                two += 1
        ptr = 0
        for i in range(zero):
            arr[ptr] = 0
            ptr += 1
        for i in range(one):
            arr[ptr] = 1
            ptr += 1
        for i in range(two):
            arr[ptr] = 2
            ptr += 1
        

#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")
        
if __name__ == "__main__":
    main()

# } Driver Code Ends