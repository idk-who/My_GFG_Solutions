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