class Customer(object):
	"""docstring for Customer"""

	@staticmethod
	def cry_out_loud():
		print "Hike my salary!!!"

	def __init__(self, arg):
		super(Customer, self).__init__()
		self.arg = arg
		