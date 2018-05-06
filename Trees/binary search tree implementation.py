class Node:
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

def insert(root, node):
	if root == None:
		root = node
	else:
		if root.data > node.data:
			if root.left == None:
				root.left = node
			else:
				insert(root.left, node)
		else:
			if root.right == None:
				root.right = node
			else:
				insert(root.right, node)

def inOrder(root):
	if root:
		inOrder(root.left)
		print root.data,
		inOrder(root.right)

def preOrder(root):
	if root:
		print root.data,
		inOrder(root.left)
		inOrder(root.right)

def postOrder(root):
	if root:
		inOrder(root.left)
		inOrder(root.right)
		print root.data,


if __name__ == '__main__':
	r = Node(50)
	insert(r,Node(30))
	insert(r,Node(20))
	insert(r,Node(40))
	insert(r,Node(70))
	insert(r,Node(60))
	insert(r,Node(80))

	inOrder(r)
	print
	preOrder(r)
	print 
	postOrder(r)

