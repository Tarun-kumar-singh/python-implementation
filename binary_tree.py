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
		self.create_tree2(new_node)
		self.create_right(new_node)

	def	create_tree2(self,node):
		data = int(input('Enter the left child of {0}'.format(node.data)))
		if(data == -1):
			return
		new_node = Node(data)
		self.create_tree2(new_node)
		node.left = new_node
		self.create_right(new_node)
		return

	def create_right(self,node):
		data = int(input('enter the right child of {0}'.format(node.data)))
		if data == -1:
			return
		new_node = Node(data)
		self.create_right(new_node)
		node.right = new_node
		self.create_tree2(new_node)
		return

	def	inorder_traversal(self):

	


b = BinaryTree()
b.create_tree()


		

