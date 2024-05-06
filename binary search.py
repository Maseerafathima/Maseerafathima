n=int(input())
l=list(map(int,input().split()))
class TreeNode:
    def _init_(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def insertIntoBST(root,value):
    if root==None:
        newnode=TreeNode(value)
        return newnode

    if root.data>value:
        root.left=insertIntoBST(root.left,value)
    else:
        root.right=insertIntoBST(root.right,value)
    return root
def InOrder(root):
    if root==None:
        return
    InOrder(root.left)
    print(root.data,end=" ")
    InOrder(root.right) 
    
root=None
for ele in l:
    root=insertIntoBST(root,ele)
InOrder(root)
