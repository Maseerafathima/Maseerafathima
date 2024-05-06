n=int(input())
l=list(map(int,input().split()))
target=int(input())
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

def SearchInBST(root,target):
    if root==None:
        return False

    elif root.data==target:
        return True
    elif root.data<target:
        return SearchInBST(root.right,target)
   
    return SearchInBST(root.left,target)

    
root=None
for ele in l:
    root=insertIntoBST(root,ele)
if SearchInBST(root,target):
    print("Target element is found")
else:
    print("Target element is not found")
