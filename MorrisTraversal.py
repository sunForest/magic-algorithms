class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def morrisTraversal(root):
    """
    inorder traversal of tree with constant space (no stack)
    @param root TreeNode
    @return list of integers
    """
    iot = []
    if root is None:
        return iot

    current = root
    while current is not None:
        # current node has no left child
        # visit it and go right
        if current.left is None:
            iot.append(current.data)
            current = current.right
        
        # current node has left child
        # we should visit left child first
        # Gist: each node with left child will be visited twice
        # In the first visit, its rightmost decendant on the left branch
        # is linked to this node with the right pointer
        # In the second visit, the modification will be restored and the
        # node itself is traversed
        else:
            previous = current.left
            while previous.right is not None and previous.right != current:
                previous = previous.right
            if previous.right is None:
                previous.right = current
                current = current.left
            else:
                previous.right = None
                iot.append(current.data)
                current = current.right
    return iot


def inorderTraversal(root):
    """
    A recursive implementation of inorder traversal
    @param root TreeNode
    @return list of integers
    """
    iot = []
    if root is None:
        return iot
    iot += inorderTraversal(root.left)
    iot.append(root.data)
    iot += inorderTraversal(root.right)
    return iot

if __name__ == '__main__':
    someTree = TreeNode(1)
    someTree.left = TreeNode(2)
    someTree.right = TreeNode(3)
    someTree.left.left = TreeNode(4)
    someTree.right.left = TreeNode(5)
    print morrisTraversal(someTree) == inorderTraversal(someTree)

