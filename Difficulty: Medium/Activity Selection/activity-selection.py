class Solution:
    def activitySelection(self, start, finish):
        timeline = [(start[i], finish[i]) for i in range(len(start))]
        timeline.sort(key = lambda x: x[1])
        
        ans = 0
        
        time = -1
        
        for s, e in timeline:
            if s > time:
                time = e
                ans += 1
        
        return ans
        
#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        # Read the start times
        start = list(map(int, input().strip().split()))

        # Read the finish times
        finish = list(map(int, input().strip().split()))

        # Create solution object and call activitySelection
        obj = Solution()
        print(obj.activitySelection(start, finish))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends