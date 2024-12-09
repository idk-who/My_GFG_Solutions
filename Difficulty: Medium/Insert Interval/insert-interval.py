#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def insertInterval(self, intervals, newInterval):
        
        ans = []
        
        ptr = 0
        
        while ptr < len(intervals) and intervals[ptr][1] < newInterval[0]:
            ans.append(intervals[ptr])
            ptr += 1
        
        if ptr < len(intervals) and intervals[ptr][0] <= newInterval[1]:
            mi = min(newInterval[0], intervals[ptr][0])
            ma = max(newInterval[1], intervals[ptr][1])
            while ptr < len(intervals) and intervals[ptr][0] <= ma:
                ma = max(ma, intervals[ptr][1])
                ptr += 1
            ans.append([mi, ma])
        else:
            ans.append(newInterval)
        
        while ptr < len(intervals):
            ans.append(intervals[ptr])
            ptr += 1        
        
        return ans
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        newEvent = list(map(int, input().split()))
        ob = Solution()
        res = ob.insertInterval(intervals, newEvent)
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            print(str(res[i][0])+','+str(res[i][1]), end = '')
            print(']', end = '')
            if i < len(res)-1:
                print(',', end='')
        print(']')
        print("~")
# } Driver Code Ends