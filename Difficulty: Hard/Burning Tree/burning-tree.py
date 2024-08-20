#User function Template for python3

class Solution:
    def parent(self,root,target):
        parentMap={}
        curr = None
        q=[]
        q.append(root)
        while q:
            curr = q.pop(0)
            if curr.data==target:
                x=curr
            if curr.left:
                parentMap[curr.left]=curr
                q.append(curr.left)
            if curr.right:
                parentMap[curr.right]=curr
                q.append(curr.right)
        return (parentMap,x)
    def minTime(self, root,target):
        # code here
        parentMap,x =self.parent(root,target)
        q=[]
        burned={
            x:True
        }
        q.append(x)
        time=0
        while q:
            size=len(q)
            isBurned=False
            while size>0:
                curr=q.pop(0)
                
                if curr in parentMap.keys() and parentMap[curr] not in burned.keys():
                    isBurned=True
                    burned[parentMap[curr]]=True
                    q.append(parentMap[curr])
                if curr.left and curr.left not in burned.keys():
                    isBurned=True
                    burned[curr.left]=True
                    q.append(curr.left)
                if curr.right and curr.right not in burned.keys():
                    isBurned=True
                    burned[curr.right]=True
                    q.append(curr.right)
                
                size-=1
            if isBurned:
                time+=1
        return time




#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends