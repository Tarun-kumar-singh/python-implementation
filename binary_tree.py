class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class BinaryTree:

	def	__init__(self):
		self.root = None

	def create_tree(self):
		data = int(input('enter root node'))
		if data == -1:
			return
		new_node = Node(data)
		self.root = new_node
		self.create_lefttree(new_node)
		self.create_righttree(new_node)

	def	create_lefttree(self,node):
		data = int(input('Enter the left child of {0}'.format(node.data)))
		if(data == -1):
			return
		new_node = Node(data)
		self.create_lefttree(new_node)
		node.left = new_node
		self.create_righttree(new_node)
		return

	def create_righttree(self,node):
		data = int(input('enter the right child of {0}'.format(node.data)))
		if data == -1:
			return
		new_node = Node(data)
		self.create_righttree(new_node)
		node.right = new_node
		self.create_lefttree(new_node)
		return

	def	inorder_traversal(self, parent):
		if parent:
			self.inorder_traversal(parent.left)
			print(parent.data)
			self.inorder_traversal(parent.right)
		return


	def preorder_traversal(self,parent):
		if parent:
			print(parent.data)
			self.preorder_traversal(parent.left)
			self.preorder_traversal(parent.right)
		return

	def	postorder_traversal(self,parent):
		if parent:
			self.postorder_traversal(parent.left)
			self.postorder_traversal(parent.right)
			print(parent.data)
		return

	def count_no_of_nodes(self, node):
		if(node):
			return  (1 + self.count_no_of_nodes(node.left) + self.count_no_of_nodes(node.right))
		else:
			return  0

	def count_no_leaves(self,node):
		if(not node):
			return
		if(not node.left and not node.right):
			return 1
		else:
			return ( self.count_no_leaves(node.left) + self.count_no_leaves(node.right))

	def	no_of_full_nodes(self,node):
		if not node:
			return 0
		if(not node.left and not node.right ):
			return 0

		return (1 if node.left and node.right else 0) + self.no_of_full_nodes(node.right) + self.no_of_full_nodes(node.left)

	def height_of_tree(self):
		

b = BinaryTree()
b.create_tree()
# print('inorder traversal...............')
# b.inorder_traversal(b.root)
# print('preorser traversal.................')
# b.preorder_traversal(b.root)
# print('post order traversal...............')
# b.postorder_traversal(b.root)
# print(b.count_no_leaves(b.root))
print(b.no_of_full_nodes(b.root))
		

