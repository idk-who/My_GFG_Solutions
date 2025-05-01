#User function Template for python3
from math import factorial

class Solution:
    def nthRowOfPascalTriangle(self, row_number):
        # Initialize the Pascal's Triangle row with 1s
        pascal_row = [1] * (row_number)
        
        # Indices to iterate through the row and calculate binomial coefficients
        left_index, right_index = 1, row_number - 2
        
        # Calculate the factorial of the row number minus 1
        numerator = factorial(row_number - 1)
        
        # Iterate through the row and calculate binomial coefficients
        while left_index <= right_index:
            # Calculate the binomial coefficient using factorials
            binomial_coefficient = numerator // (factorial(row_number - left_index - 1) * factorial(left_index))
            
            # Take the modulo to prevent overflow and keep the result within bounds
            pascal_row[left_index] = pascal_row[right_index] = binomial_coefficient % (10**9 + 7)
            
            # Move indices towards the center of the row
            left_index, right_index = left_index + 1, right_index - 1
        
        # Return the final Pascal's Triangle row
        return pascal_row


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.nthRowOfPascalTriangle(n)
        for x in ans:
            print(x, end=" ")
        print()
        tc = tc - 1
        print("~")
# } Driver Code Ends