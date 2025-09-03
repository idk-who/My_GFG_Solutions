"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        if not head or not head.next:
            return head
            
        curr = head
        prev = curr.prev
        nxt = curr.next
        
        while curr:
            curr.next = prev
            curr.prev = nxt
            
            prev = curr
            curr = nxt
            nxt = nxt.next if nxt else None
        
        return prev
        
        
        
        