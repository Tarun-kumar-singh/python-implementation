
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class linklist_():
			def __init__(self):
				self.head = None

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

			def insertBegining(self):
				data = int(input('Enter data to insert at insert at begining'))
				new_node =Node(data)
				new_node.next = self.head
				self.head = new_node
				return

			def insertEnd(self):
				data = int(input('Enter data to insert at the end '))
				new_node = Node(data)
				t = self.head
				while t.next:
					t = t.next
				t.next = new_node
				return

			def printList(self):
				t = self.head
				while t != None:
					print(t.data)
					t = t.next
				return
				
			def no_of_count(self):	
				t = self.head
				count = 0
				while t:
					count = count + 1
					t = t.next
				return count	 

						

						
l = linklist()	
l.createList()
# l.printList()
# l.insertEnd()
# l.printList()
# l.insertBegining()
# l.printList()
print(l.no_of_count())
 


				




 						