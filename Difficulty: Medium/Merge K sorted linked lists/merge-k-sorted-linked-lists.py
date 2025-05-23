#User function Template for python3
'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''

from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, arr):
        Dummy = Node(-1)
        
        prev = Dummy
        
        pq = []
        
        for node in arr:
            if node:
                heappush(pq, (node.data, node))
        
        while pq:
            _, node = heappop(pq)
            prev.next = node
            prev = prev.next
            if node.next:
                heappush(pq, (node.next.data, node.next))
        
        return Dummy.next                                       
        


#{ 
 # Driver Code Starts
import heapq


class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

    # To compare nodes in the heap
    def __lt__(self, other):
        return self.data < other.data


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lists = []
        for _ in range(n):
            values = list(map(int, input().split()))
            head = None
            temp = None
            for value in values:
                newNode = Node(value)
                if head is None:
                    head = newNode
                    temp = head
                else:
                    temp.next = newNode
                    temp = temp.next
            lists.append(head)

        sol = Solution()
        head = sol.mergeKLists(lists)
        printList(head)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends