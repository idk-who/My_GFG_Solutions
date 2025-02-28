#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends

class Solution:
    def evaluate(self, arr):
        stack=[]
        for i in arr:
            if i=='+' or i=='-' or i=='/' or i=='*':
                b=stack.pop()
                a=stack.pop()
                if i=='+':
                    stack.append(int(a)+int(b))
                elif i=='-':
                    stack.append(int(a)-int(b))
                elif i=='*':
                    stack.append(int(a)*int(b))
                elif i=='/':
                    stack.append(int(int(a) / int(b)))
            else:
                stack.append(i)
        return stack.pop()


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = input().split()
        solution = Solution()
        print(solution.evaluate(arr))
        print("~")

# } Driver Code Ends