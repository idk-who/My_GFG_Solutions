class Solution:
    def maxPartitions(self , s):
        last_occ = [-1]*26
        
        for i, c in enumerate(s):
            last_occ[ord(c)-ord('a')] = i
        
        end = 0
        ans = 0
        for i, c in enumerate(s):
            end = max(end, last_occ[ord(c)-ord('a')])
            
            if i == end:
                ans += 1
        
        return ans


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends