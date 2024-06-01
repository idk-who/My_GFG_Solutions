
class Solution:
    def oddEven(self, s : str) -> str:
        freq = [0]*26
        
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
                
                
        nx = 0
        ny = 0
        
        for i in range(26):
            if i & 1 and freq[i] > 0 and not freq[i] & 1:
                nx += 1
            if not i & 1 and freq[i] & 1:
                ny += 1
                
        return "EVEN" if (nx + ny) % 2 == 0 else "ODD"



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends