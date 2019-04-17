class Dog(object):
	def __init__(self, name):
		self.name = name
class UltraDog(Dog):
	def __init__(self, name, type):
		super().__init__(name)
		self.type = type
def empty_func():
	pass