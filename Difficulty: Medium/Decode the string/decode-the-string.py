
class Solution:
    def decodedString(self, s):
        ans = ""
        stack = []
        curr = ""
        ptr = 0
        
        while ptr < len(s):
            if s[ptr].isdigit():
                num = 0
                while s[ptr].isdigit():
                    num = num*10 + int(s[ptr])
                    ptr += 1
                stack.append(curr)
                stack.append(num)
                
                curr = ""
                ptr += 1
            elif s[ptr] == ']':
                num = stack.pop()
                new_curr = stack.pop()
                for i in range(num):
                    new_curr += curr
                curr = new_curr
                ptr += 1
            else:
                curr += s[ptr]
                ptr += 1
        
        return curr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends