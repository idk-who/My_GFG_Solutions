class Solution:
    def generateBinary(self, N):
        # code here
        q = deque()
        q.append("1")
        res = []
        for _ in range(N):
            curr = q.popleft()
            res.append(curr)
            q.append(curr+"0")
            q.append(curr+"1")
        return res