'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque

class Solution:
    
    def __init__(self):
        self.parent_map={}
        self.target_node=None
        self.target=None
        
    def find_parent_map(self,curr,parent):
        if curr:
            if curr.data==self.target:
                self.target_node=curr
            self.parent_map[curr]=parent
            self.find_parent_map(curr.left,curr)
            self.find_parent_map(curr.right,curr)
        
    def minTime(self, root, target):
        ans=-1
        self.target=target
        self.find_parent_map(root,None)
        q=deque([self.target_node])
        visited={self.target_node}
        while q:
            size=len(q)
            for _ in range(size):
                curr=q.popleft()
                for v in [curr.left,curr.right,self.parent_map[curr]]:
                    if v and v not in visited:
                        q.append(v)
                        visited.add(v)
            ans+=1
        return ans