from binary_searchtree import binarySearchTree
from binary_tree import BinaryTree

bt = BinaryTree()
bt.create_tree()


a = [-5]

def isBst(node):

    if not node:
        print('Tree is empty!')
        return False
    return isBst_check(node)


def isBst_check(node):

    if node:
        isBst_check(node.left)
        if(a[0] < node.data):
            a[0] = node.data
            isBst_check(node.right)
        else: return False
    return True


print(isBst(bt.root))
