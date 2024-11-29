#User function Template for python3
class Solution:
    def addBinary(self, s1, s2):
        # code here
        decimal_number1 = int(s1, 2)
        decimal_number2 = int(s2, 2)
        result = decimal_number1 + decimal_number2
        binary_number = bin(result)[2:]
        
        return binary_number


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends