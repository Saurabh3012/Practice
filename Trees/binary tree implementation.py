class Node:
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right


'''
           1
       /       \
      2          3
    /   \       /  \
   4    None  None  None
  /  \
None None

'''

if __name__ == '__main__':

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
