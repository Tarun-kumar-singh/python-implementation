class Node:
    def __init__(self, data):
        self.leftsubtree = None
        self.rightsubtree = None
        self.data = data


class binarySearchTree:
    def __init__(self):
        self.root = None

    def createTree(self):
        rootdata = int(input('enter the root data '))
        self.root = Node(rootdata)
        while (True):
            data = int(input('enter data'))
            if (data == -1):
                return
            self.insertData(data)

    def insertData(self, data):
        t = self.root
        while( t.leftsubtree or t.rightsubtree):
             if(data > t.data):
                 if(not t.rightsubtree):
                     break
                 else:
                    t = t.rightsubtree
             else:
                 if (not t.leftsubtree):
                     break
                 else:
                     t = t.leftsubtree

        if(data > t.data ):
            t.rightsubtree = Node(data)
            return
        else:
            t.leftsubtree = Node(data)
            return

    def inorder_traversal(self, parent):
        if parent:
            self.inorder_traversal(parent.leftsubtree)
            print(parent.data)
            self.inorder_traversal(parent.rightsubtree)
        return

    def preorder_traversal(self,parent):
        if(parent):
            print(parent.data)
            self.preorder_traversal(parent.leftsubtree)
            self.preorder_traversal(parent.rightsubtree)
        return



b = binarySearchTree()
b.createTree()
print('inorder traversal....')
b.inorder_traversal(b.root)
print('pre order traversal....')
b.preorder_traversal(b.root)