#User function Template for python3

'''
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
'''

class Solution():
    def cloneGraph(self, node):
        
        # Fix for judge's code doing to many recursion calls
        import sys
        sys.setrecursionlimit(10**4)
        # end of fix
        
        # N leeks from the judge's code
        #N = 10**4
        nodes = [Node(i, []) for i in range(N)]
        visited = [False] * N
        s = [node]
        while s:
            u = s.pop()
            if visited[u.val]:
                continue
            visited[u.val] = True
            copy_u = nodes[u.val]
            for v in u.neighbors:
                copy_u.neighbors.append(nodes[v.val])
                if not visited[v.val]:
                    s.append(v)
        return nodes[node.val]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from queue import Queue
import sys

sys.setrecursionlimit(10**6)


class Node:

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def compare(prev, new, prev_vis=set(), new_vis=set()):
    if prev == new:
        return False
    if not prev or not new:
        if (not prev and new) or (prev and not new):
            return False
        return True

    if prev in prev_vis or new in new_vis:
        if (prev in prev_vis and new not in new_vis) or (prev not in prev_vis
                                                         and new in new_vis):
            return False
        return True
    prev_vis.add(prev)
    new_vis.add(new)

    if prev.val != new.val:
        return False

    prev_n = len(prev.neighbors)
    new_n = len(prev.neighbors)
    if prev_n != new_n:
        return False

    prev.neighbors.sort(key=lambda x: x.val)
    new.neighbors.sort(key=lambda x: x.val)
    for i in range(prev_n):
        if not compare(prev.neighbors[i], new.neighbors[i], prev_vis, new_vis):
            return False

    return True


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        v = [Node(i) for i in range(N)]
        for i in range(N):
            v[i].neighbors = [v[int(i)] for i in input().split()]
        ob = Solution()
        ans = ob.cloneGraph(v[0])
        # if ans == v[0]:
        #     print(0)
        print("true" if compare(v[0], ans) else "false")
        print("~")

# } Driver Code Ends