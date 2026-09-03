class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def search(node, key):
    if node is None:
        return False
    if node.key == key:
        return True
    return search(node.left, key) or search(node.right, key)

n = int(input("Enter number of nodes: "))
root = None

print("Enter", n, "values to insert in BST:")
for _ in range(n):
    val = int(input())
    root = insert(root, val)

key = int(input("Enter key to search: "))

if search(root, key):
    print("Key", key, "found in BST.")
else:
    print("Key", key, "NOT found in BST.")