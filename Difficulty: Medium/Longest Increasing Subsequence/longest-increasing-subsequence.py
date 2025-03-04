from bisect import bisect_left
class Solution:
    def lis(self, arr):
        # code here
        seq = []
        
        for i in arr:
            if not seq or i > seq[-1]:
                seq.append(i)
            else:
                ind = bisect_left(seq, i)
                seq[ind] = i
        
        return len(seq)



#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.lis(a))
        print("~")
# } Driver Code Ends