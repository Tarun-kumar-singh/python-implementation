# creating a list of length 7 in which 7th node points back to the 3rd
 # element to create loop

class Node():

	def __init__(self,data):
		self.data = data
		self.next = None

class loopList():
	
	def __init__(self):
		self.head = None

	def createloop(self):
		print('Enter 8 data')
		for i in range(8):
			data = int(input('enter {0} data'.format(i+1)))
			new_node = Node(data)
			if(i == 0):
				self.head = new_node
				t = new_node
				continue

			if ((i + 1) == 4):
				loopPointer = new_node

			if((i + 1) == 8):
				t.next = new_node
				t = new_node
				new_node.next = loopPointer
				continue

			t.next = new_node
			t = new_node

	def createList(self):
				d = int(input('Enter no of data'))
				for i in range(d):
					data = int(input('enter {0} data'.format(i + 1)))
					if i == 0:
						self.head = Node(data)
						t = self.head
						continue
					new_node = Node(data)
					t.next = new_node
					t = new_node
				return

	def printLoop(self):
		t = self.head
		while(t):
			print(t.data)
			t = t.next

	def isLoop(self):

		if self.head == None:
			print('List is empty')
			return
		slow = self.head
		fast = self.head
		while(slow and fast):
			slow = slow.next
			fast = fast.next.next
			if(slow == fast):
				print('Loop is detected at {0}'.format(slow.data))
				return slow

		print('loop is not present')
		return None

	def loopLength(self):
		lp = self.isLoop()
		if(lp):
			lp2 = lp.next
			count = 0
			while (lp != lp2):
				count = count + 1
				lp2 = lp2.next
			return count + 1

		return None

	def	listLength(self):


	# def loopPoint(self):
	# 	pass




l = loopList()
# l.createList()
l.createloop()
# l.printLoop()
# l.isLoop()
print(l.loopLength())

 




			
		