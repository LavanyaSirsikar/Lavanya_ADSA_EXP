class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def insert(root,key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left=insert(root.left,key)
    else:
        root.right=insert(root.right,key)
    return root     

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val,end=" ")
        preorder(root.left)
        preorder(root.right)                    

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end=" ")

if __name__=="__main__":
    root=None
    keys=[50,30,70,20,40,60,80]

for k in keys:
    root=insert(root,k)

print("Inorder Traversal:\n")
inorder(root)
print("\n")

print("Preorder Traversal:\n")
preorder(root)
print("\n")

print("Postorder Traversal:\n")
postorder(root)
print()
