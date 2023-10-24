class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def search(k, p):
    if p is None:
        return None
    elif k == p.key:
        return p
    elif k < p.key:
        return search(k, p.left)
    else:
        return search(k, p.right)

def addNode(k, p):
    if p is None:
        return Node(k)
    elif k != p.key:
        if k < p.key:
            p.left = addNode(k, p.left)
        else:
            p.right = addNode(k, p.right)
    return p

def removeNode(k, p):
    if p is not None:
        if k < p.key:
            p.left = removeNode(k, p.left)
        elif k > p.key:
            p.right = removeNode(k, p.right)
        else:
            if p.left is None and p.right is None:
                p = None
            elif p.left is None:
                p = p.right
            elif p.right is None:
                p = p.left
            else:
                p.left, r = extractMaxNode(p.left)
                r.left = p.left
                r.right = p.right
                p = r
    return p

def extractMaxNode(p):
    if p.right is None:
        return p.left, p
    else:
        p.right, r = extractMaxNode(p.right)
        return p, r

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.key)  # ノードの値を表示
        inorder_traversal(node.right)

root = None
root = addNode(5, root)
root = addNode(2, root)
root = addNode(7, root)
root = addNode(1, root)
root = addNode(8, root)
root = addNode(4, root)
root = addNode(3, root)
root = addNode(12, root)
root = removeNode(5, root)
root = removeNode(7, root)

# 中順トラバーサルを実行してノードの値を表示
inorder_traversal(root)
# print(root.key)
