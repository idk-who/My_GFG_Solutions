'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def addTwoLists(self, head1, head2):
        def reverse(head):
            prv=None
            cur=head
            while cur:
                nxt=cur.next
                cur.next=prv
                prv=cur
                cur=nxt
            return prv
        ret=Node(0)
        cur=ret
        cur1=reverse(head1)
        cur2=reverse(head2)
        carry=0
        while cur1 or cur2:
            cur.data=(cur1.data if cur1 else 0)+(cur2.data if cur2 else 0)+carry
            carry=cur.data//10
            cur.data%=10
            cur1=cur1.next if cur1 else None
            cur2=cur2.next if cur2 else None
            cur.next=Node(0)
            cur=cur.next
        if carry==1:
            cur.data=1
        ret=reverse(ret)
        while ret.data==0:
            ret=ret.next
        return ret