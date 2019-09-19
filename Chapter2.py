# R-2.4
class Flower:
	def __init__(self, name, PetalNumber, price):
		self._name = name
		self._PetalNumber = PetalNumber
		self._price = price
	def set_name(self, name):
		self._name = name
	def set_PetalNumber(self, PetalNumber):
		self._PetalNumber = PetalNumber
	def set_price(self, price):
		self._price = price
	def get_name(self):
		return self._name
	def get_PetalNumber(self):
		return self._PetalNumber
	def get_price(self):
		return self._price
	def fl_describe(self):
		print("""
              name: {0}
              petal: {1}
              price: {2}
              """.format(self._name, self._PetalNumber, self._price))


obj1 = Flower('rose', '10', '12.6')
obj2 = Flower('lily', '5', '20.3')

print(obj1.get_name())
print(obj1.get_PetalNumber())
print(obj1.get_price())

print(obj2.get_name())
print(obj2.get_PetalNumber())
print(obj2.get_price())

obj2.set_name('lilies')
obj2.fl_describe()



# R-2.5
class CreditCard:
	"""docstring for CreditCard"""
	def __init__(self, customer, bank, account, credit_limit):
		self._customer = customer
		self._bank = bank
		self._account = account
		self._credit_limit = credit_limit
		self._balance = 0
	def get_customer(self):
		return self._customer
	def get_bank(self):
		return self._bank
	def get_account(self):
		return self._account
	def get_credit_limit(self):
		return self._credit_limit
	def get_balance(self):
		return self._balance
	def charge(self, price):
		try:
			if price + self._balance > self._credit_limit:
				return False
			else:
				self._balance += price 
				return True
		except(TypeError):
			print('Please enter numerical type.')
	def make_payment(self, amount):      
		"""Process customer payment that reduces balance."""
		try:
			self._balance -= amount
		except(TypeError):
			print('Please enter numerical type.')

# test error
if __name__ == '__main__':
  a = CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500)
  print(a.charge(10))
  print(a.charge('df'))
  a.make_payment(5)
  a.make_payment("dfs")

		

# R-2.6 
# If the parameter to the make payment method of the CreditCard class were a negative number, 
# that would have the effect of raising the balance on the account. 
# Revise the implementation so that it raises a ValueError if a negative value is sent.
class CreditCard:
	"""docstring for CreditCard"""
	def __init__(self, customer, bank, account, credit_limit):
		self._customer = customer
		self._bank = bank
		self._account = account
		self._credit_limit = credit_limit
		self._balance = 0
	def get_customer(self):
		return self._customer
	def get_bank(self):
		return self._bank
	def get_account(self):
		return self._account
	def get_credit_limit(self):
		return self._credit_limit
	def get_balance(self):
		return self._balance
	def charge(self, price):
		try:
			if price + self._balance > self._credit_limit:
				return False
			else:
				self._balance += price 
				return True
		except(TypeError):
			print('Please enter numerical type.')
	def make_payment(self, amount):      
		"""Process customer payment that reduces balance."""
		try:
			self._balance -= amount
			if amount < 0:
				raise ValueError('ValueError. Negative amount.')
		except(TypeError):
			print('Please enter numerical type.')
		except ValueError as ve:
			print(ve)

# test error
if __name__ == '__main__':
  a = CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500)
  print(a.charge(10))
  print(a.charge('df'))
  a.make_payment(5)
  a,make_payment(-5)
  a.make_payment("dfs") 


# R-2.7 
# The CreditCard class of Section 2.3 initializes the balance of a new account to zero. 
# Modify that class so that a new account can be given a nonzero balance using an optional 
# fifth parameter to the constructor. The four-parameter constructor syntax should continue 
# to produce an account with zero balance.
class CreditCard:
	"""docstring for CreditCard"""
	def __init__(self, customer, bank, account, credit_limit, balance = 0):
		self._customer = customer
		self._bank = bank
		self._account = account
		self._credit_limit = credit_limit
		self._balance = balance
	def get_customer(self):
		return self._customer
	def get_bank(self):
		return self._bank
	def get_account(self):
		return self._account
	def get_credit_limit(self):
		return self._credit_limit
	def get_balance(self):
		return self._balance
	def charge(self, price):
		try:
			if price + self._balance > self._credit_limit:
				return False
			else:
				self._balance += price 
				return True
		except(TypeError):
			print('Please enter numerical type.')
	def make_payment(self, amount):      
		"""Process customer payment that reduces balance."""
		try:
			self._balance -= amount
			if amount < 0:
				raise ValueError('ValueError. Negative amount.')
		except(TypeError):
			print('Please enter numerical type.')
		except ValueError as ve:
			print(ve)


# R-2.8 
# Modify the declaration of the first for loop in the CreditCard tests, from Code Fragment 2.3,
# so that it will eventually cause exactly one of the three credit cards to go over its credit limit. 
# Which credit card is it?
if __name__ == '__main__':
	wallet = [ ]
	wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500) ) 
	wallet.append(CreditCard('Leo Bowman', 'California Federal', '3485 0399 3395 1954', 3500) ) 
	wallet.append(CreditCard('Mark Bowman', 'California Finance', '5391 0375 9387 5309', 5000) ) 
	wallet[0].charge(2600) 
	wallet[1].charge(2600) 
	wallet[2].charge(2600)
	for c in range(3):
		print('Customer = ', wallet[c].get_customer()) 
		print('Bank = ', wallet[c].get_bank())
		print('Account = ', wallet[c].get_account()) 
		print('Limit = ', wallet[c].get_credit_limit())
		print('Balance = ', wallet[c].get_balance()) 
		while wallet[c].get_balance( ) > 2000:
			wallet[c].make_payment(2000)
			print('New balance = ', wallet[c].get_balance()) 
		print( )


# R-2.9
# Implement the __sub__ method for the Vector class of Section 2.3.3, 
# so that the expression u-v returns a new vector instance representing the difference between two vectors.
class Vector:
	"""Represent a vector in a multidimensional space."""
	def __init__(self, d):
		"""Create d-dimensional vector of zeros.""" 
		self._coords = [0] * d

	def __len__(self):
		"""Return the dimension of the vector."""
		return len(self._coords)
	def __getitem__(self, j):
		"""Return jth coordinate of vector.""" 
		return self._coords[j]
	def __setitem__(self, j, val):
		"""Set jth coordinate of vector to given value.""" 
		self._coords[j] = val
	def __add__(self, other):
		"""Return sum of two vectors."""
		if len(self) != len(other): # relies on __len__ method
			raise ValueError('dimensions must agree')
		result = Vector(len(self)) 
		for j in range(len(self)):
			result[j] = self[j] + other[j] 
		return result  # start with vector of zeros
	def __eq__(self, other):
		"""Return True if vector has same coordinates as other.""" 
		return self._coords == other._coords
	def __ne__(self, other):
		"""Return True if vector differs from other."""
		return not self == other # rely on existing __eq__ definition
	def __str__(self):
		"""Produce string representation of vector."""
		return '<' + str(self._coords)[1:-1] + '>'    # adapt list representation
	def __sub__(self, other):
		"""Return difference of two vectors."""
		if len(self) != len(other):
			raise ValueError('dimensions must agree')
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] - other[j]
		return result

if __name__ == '__main__':
	v = Vector(5)
	v[1]= 10
	v[-1] = 40
	print(v[4])
	u = v + v 
	print(u)
	u = v - v 
	print(u)


# R-2.10
# Implement the __neg__ method for the Vector class of Section 2.3.3, 
# so that the expression −v returns a new vector instance whose coordinates 
# are all the negated values of the respective coordinates of v.
class Vector:
	"""Represent a vector in a multidimensional space."""
	def __init__(self, d):
		"""Create d-dimensional vector of zeros.""" 
		self._coords = [0] * d

	def __len__(self):
		"""Return the dimension of the vector."""
		return len(self._coords)
	def __getitem__(self, j):
		"""Return jth coordinate of vector.""" 
		return self._coords[j]
	def __setitem__(self, j, val):
		"""Set jth coordinate of vector to given value.""" 
		self._coords[j] = val
	def __add__(self, other):
		"""Return sum of two vectors."""
		if len(self) != len(other): # relies on __len__ method
			raise ValueError('dimensions must agree')
		result = Vector(len(self)) 
		for j in range(len(self)):
			result[j] = self[j] + other[j] 
		return result  # start with vector of zeros
	def __eq__(self, other):
		"""Return True if vector has same coordinates as other.""" 
		return self._coords == other._coords
	def __ne__(self, other):
		"""Return True if vector differs from other."""
		return not self == other # rely on existing __eq__ definition
	def __str__(self):
		"""Produce string representation of vector."""
		return '<' + str(self._coords)[1:-1] + '>'    # adapt list representation
	def __sub__(self, other):
		"""Return difference of two vectors."""
		if len(self) != len(other):
			raise ValueError('dimensions must agree')
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] - other[j]
		return result
	def __neg__(self):
		"""Return all the negated values of the respective coordinates of v"""
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = -self[j]
		return result

if __name__ == '__main__':
	v = Vector(5)
	start = 10
	for i in range(5):
		start += i 
		v[i] = start
	print(v)
	u = - v 
	print(u)


# R-2.11
# In Section 2.3.3, we note that our Vector class supports a syntax such as v = u + [5, 3, 10, −2, 1], 
# in which the sum of a vector and list returns a new vector. 
# However, the syntax v = [5, 3, 10, −2, 1] + u is illegal. 
# Explain how the Vector class definition can be revised so that this syntax generates a new vector.

# uese the iterable method, add one by one



# R-2.12
# Implement the __mul__ method for the Vector class of Section 2.3.3, 
# so that the expression v * 3 returns a new vector with coordinates that are 3 times the respective coordinates of v.
class Vector:
	"""Represent a vector in a multidimensional space."""
	def __init__(self, d):
		"""Create d-dimensional vector of zeros.""" 
		self._coords = [0] * d

	def __len__(self):
		"""Return the dimension of the vector."""
		return len(self._coords)
	def __getitem__(self, j):
		"""Return jth coordinate of vector.""" 
		return self._coords[j]
	def __setitem__(self, j, val):
		"""Set jth coordinate of vector to given value.""" 
		self._coords[j] = val
	def __add__(self, other):
		"""Return sum of two vectors."""
		if len(self) != len(other): # relies on __len__ method
			raise ValueError('dimensions must agree')
		result = Vector(len(self)) 
		for j in range(len(self)):
			result[j] = self[j] + other[j] 
		return result  # start with vector of zeros
	def __eq__(self, other):
		"""Return True if vector has same coordinates as other.""" 
		return self._coords == other._coords
	def __ne__(self, other):
		"""Return True if vector differs from other."""
		return not self == other # rely on existing __eq__ definition
	def __str__(self):
		"""Produce string representation of vector."""
		return '<' + str(self._coords)[1:-1] + '>'    # adapt list representation
	def __sub__(self, other):
		"""Return difference of two vectors."""
		if len(self) != len(other):
			raise ValueError('dimensions must agree')
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] - other[j]
		return result
	def __neg__(self):
		"""Return all the negated values of the respective coordinates of v"""
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = -self[j]
		return result
	def __mul__(self, val):
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] * val 
		return result

if __name__ == '__main__':
	v = Vector(5)
	start = 10
	for i in range(5):
		start += i 
		v[i] = start
	print(v)
	u = v * 3 
	print(u)


# R-2.13
# Exercise R-2.12 asks for an implementation of __mul__ , for the Vector class of Section 2.3.3, 
# to provide support for the syntax v * 3. Implement the __rmul__ method, 
# to provide additional support for syntax 3 * v.
class Vector:
	"""Represent a vector in a multidimensional space."""
	def __init__(self, d):
		"""Create d-dimensional vector of zeros.""" 
		self._coords = [0] * d

	def __len__(self):
		"""Return the dimension of the vector."""
		return len(self._coords)
	def __getitem__(self, j):
		"""Return jth coordinate of vector.""" 
		return self._coords[j]
	def __setitem__(self, j, val):
		"""Set jth coordinate of vector to given value.""" 
		self._coords[j] = val
	def __add__(self, other):
		"""Return sum of two vectors."""
		if len(self) != len(other): # relies on __len__ method
			raise ValueError('dimensions must agree')
		result = Vector(len(self)) 
		for j in range(len(self)):
			result[j] = self[j] + other[j] 
		return result  # start with vector of zeros
	def __eq__(self, other):
		"""Return True if vector has same coordinates as other.""" 
		return self._coords == other._coords
	def __ne__(self, other):
		"""Return True if vector differs from other."""
		return not self == other # rely on existing __eq__ definition
	def __str__(self):
		"""Produce string representation of vector."""
		return '<' + str(self._coords)[1:-1] + '>'    # adapt list representation
	def __sub__(self, other):
		"""Return difference of two vectors."""
		if len(self) != len(other):
			raise ValueError('dimensions must agree')
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] - other[j]
		return result
	def __neg__(self):
		"""Return all the negated values of the respective coordinates of v"""
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = -self[j]
		return result
	def __mul__(self, val):
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] * val 
		return result
	def __rmul__(self, val):
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = val * self[j]
		return result

if __name__ == '__main__':
	v = Vector(5)
	start = 10
	for i in range(5):
		start += i 
		v[i] = start
	print(v)
	u = 3 * v
	print(u)


# R-2.14
# Implement the __mul__ method for the Vector class of Section 2.3.3, 
# so that the expression u * v returns a scalar that represents the dot product of the vectors, 
# that is, ∑d i=1 ui · vi .
class Vector:
	"""Represent a vector in a multidimensional space."""
	def __init__(self, d):
		"""Create d-dimensional vector of zeros.""" 
		self._coords = [0] * d

	def __len__(self):
		"""Return the dimension of the vector."""
		return len(self._coords)
	def __getitem__(self, j):
		"""Return jth coordinate of vector.""" 
		return self._coords[j]
	def __setitem__(self, j, val):
		"""Set jth coordinate of vector to given value.""" 
		self._coords[j] = val
	def __add__(self, other):
		"""Return sum of two vectors."""
		if len(self) != len(other): # relies on __len__ method
			raise ValueError('dimensions must agree')
		result = Vector(len(self)) 
		for j in range(len(self)):
			result[j] = self[j] + other[j] 
		return result  # start with vector of zeros
	def __eq__(self, other):
		"""Return True if vector has same coordinates as other.""" 
		return self._coords == other._coords
	def __ne__(self, other):
		"""Return True if vector differs from other."""
		return not self == other # rely on existing __eq__ definition
	def __str__(self):
		"""Produce string representation of vector."""
		return '<' + str(self._coords)[1:-1] + '>'    # adapt list representation
	def __sub__(self, other):
		"""Return difference of two vectors."""
		if len(self) != len(other):
			raise ValueError('dimensions must agree')
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] - other[j]
		return result
	def __neg__(self):
		"""Return all the negated values of the respective coordinates of v"""
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = -self[j]
		return result
	def __mul__(self, other):
		result = Vector(len(self))
		if isinstance(other, (float, int)):
			for j in range(len(self)):
				result[j] = self[j] * val 
			return result
		elif isinstance(other, (list, Vector)):
			if len(self) != len(other):
				raise ValueError('Dimensions must agree!')
			for j in range(len(self)):
				result[j] = self[j] * other[j]
			return result
	def __rmul__(self, val):
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = val * self[j]
		return result

if __name__ == '__main__':
	v = Vector(5)
	start = 10
	for i in range(5):
		start += i 
		v[i] = start
	print('v: ', v)
	u1 = 3 * v
	print('u1: ', u1)
	m = [4, 3, 1, 2, 1]
	u2 = v * m 
	print('u2: ', u2)
	m1 = Vector(5)
	start1 = 1
	for i in range(5):
		start1 += i 
		m1[i] = start1
	print('m1: ', m1)
	u3 = v * m1
	print('u3: ', u3)


# R-2.15
# The Vector class of Section 2.3.3 provides a constructor that takes an integer d, 
# and produces a d-dimensional vector with all coordinates equal to 0. 
# Another convenient form for creating a new vector would be to send the constructor a parameter 
# that is some iterable type representing a sequence of numbers, 
# and to create a vector with dimension equal to the length of that sequence 
# and coordinates equal to the sequence values. 
# For example, Vector([4, 7, 5]) would produce a three-dimensional vector with coordi- nates <4, 7, 5>. 
# Modify the constructor so that either of these forms is acceptable; that is, 
# if a single integer is sent, it produces a vector of that dimension with all zeros, 
# but if a sequence of numbers is provided, it pro- duces a vector with coordinates based on that sequence.
class Vector:
	"""Represent a vector in a multidimensional space."""
	def __init__(self, d):
		if isinstance(d, int):
			"""Create d-dimensional vector of zeros.""" 
			self._coords = [0] * d
		elif isinstance(d, (list, tuple)):
			self._coords = [val for val in d]
		else:
			raise TypeError('wrong type')

	def __len__(self):
		"""Return the dimension of the vector."""
		return len(self._coords)
	def __getitem__(self, j):
		"""Return jth coordinate of vector.""" 
		return self._coords[j]
	def __setitem__(self, j, val):
		"""Set jth coordinate of vector to given value.""" 
		self._coords[j] = val
	def __add__(self, other):
		"""Return sum of two vectors."""
		if len(self) != len(other): # relies on __len__ method
			raise ValueError('dimensions must agree')
		result = Vector(len(self)) 
		for j in range(len(self)):
			result[j] = self[j] + other[j] 
		return result  # start with vector of zeros
	def __eq__(self, other):
		"""Return True if vector has same coordinates as other.""" 
		return self._coords == other._coords
	def __ne__(self, other):
		"""Return True if vector differs from other."""
		return not self == other # rely on existing __eq__ definition
	def __str__(self):
		"""Produce string representation of vector."""
		return '<' + str(self._coords)[1:-1] + '>'    # adapt list representation
	def __sub__(self, other):
		"""Return difference of two vectors."""
		if len(self) != len(other):
			raise ValueError('dimensions must agree')
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] - other[j]
		return result
	def __neg__(self):
		"""Return all the negated values of the respective coordinates of v"""
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = -self[j]
		return result
	def __mul__(self, other):
		result = Vector(len(self))
		if isinstance(other, (float, int)):
			for j in range(len(self)):
				result[j] = self[j] * val 
			return result
		elif isinstance(other, (list, Vector)):
			if len(self) != len(other):
				raise ValueError('Dimensions must agree!')
			for j in range(len(self)):
				result[j] = self[j] * other[j]
			return result
	def __rmul__(self, val):
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = val * self[j]
		return result

if __name__ == '__main__':
	v1 = Vector(5)
	print('v1: ', v1)
	v2 = Vector([5, 6, 7])
	print('v2: ', v2)


# R-2.16
# Our Range class, from Section 2.3.5, relies on the formula max(0, (stop − start + step − 1) // step)
# to compute the number of elements in the range. 
# It is not immediately evident why this formula provides the correct calculation, 
# even if assuming a positive step size. Justify this formula, in your own words.

max(0, (stop - start + step - 1) // step)
# don't know how to explain but by examination, the formula is right


# R-2.17
# Draw a class inheritance diagram for the following set of classes:
# • Class Goat extends object and adds an instance variable _tail and methods milk() and jump().
# • Class Pig extends object and adds an instance variable _nose and methods eat(food) and wallow().
# • Class Horse extends object and adds instance variables _height and _color, and methods run() and jump().
# • Class Racer extends Horse and adds a method race().
# • Class Equestrian extends Horse, adding an instance variable _weight and methods trot() and is_trained().


# R-2.18
# Give a short fragment of Python code that uses the progression classes from Section 2.4.2 
# to find the 8th value of a Fibonacci progression that starts with 2 and 2 as its first two values.
class Progression:
	"""Iterator producing a generic progression. 
	Default iterator produces the whole numbers 0, 1, 2, ... """
	def __init__(self, start = 0):
		"""Initialize current to the first value of the progression."""
		self._current = start 
	def _advance(self):
		"""Update self._current to a new value.
		This should be overridden by a subclass to customize progression.
		By convention, if current is set to None, this designates the end of a finite progression."""
		self.current += 1
	def __next__(self):
		"""Return the next element, or else raise StopIteration error."""
		if self._current is None:        # our convention to end a progression
			raise StopIteration()
		else:
			answer = self._current       # record current value to return
			self._advance()              # advance to prepare for next time
			return answer                # return the answer
	def iter(self):
		"""By convention, an iterator must return itself as an iterator."""
		return self
	def print_progression(self, n):
		"""Print next n values of the progression."""
		print(' '.join(str(next(self)) for j in range(n)))

class FibonacciProgression(Progression):
	"""Iterator producing a generalized Fibonacci progression."""
	def __init__(self, first = 0, second = 0):
		"""Create a new fibonacci progression. first = 2, second = 2"""
		super().__init__(first)         # start progression at first
		self._prev = second - first     # fictitious value preceding the first
	def _advance(self):
		"""Update current value by taking sum of previous two."""
		self._prev, self._current = self._current, self._prev + self._current

if __name__ == '__main__':
	print('Fibonacci progression with start values 2 and 2: ')
	FibonacciProgression(2, 2).print_progression(10)


# R-2.19
# When using the ArithmeticProgression class of Section 2.4.2 with an increment of 128 and a start of 0, 
# how many calls to next can we make before we reach an integer of 263 or larger?
class ArithmeticProgression(Progression):         # inherit from Progression
	"""Iterator producing an arithmetic progression."""
	def __init__(self, increment = 1, start = 0):
		"""Create a new arithmetic progression.
		increment: the fixed constant to add to each term(default 1)
		start: the first term of the progression(default 0)"""
		super().__init__(start)   # initialize base class 
		self._increment = increment
	def _advance(self):     # override inherited version 
		"""Update current value by adding the fixed increment."""
		self._current += self._increment

if __name__ == '__main__':
	print('Arithmetic progression with start values 0 and increment of 128: ')
	ArithmeticProgression(128, 0).print_progression(4)
	
# 3 calls


# R-2.20
# What are some potential efficiency disadvantages of having very deep inheritance trees, 
# that is, a large set of classes, A, B, C, and so on, such that B extends A, C extends B, D extends C, etc.?

# The only efficiency problems for a deep inheritance tree that I can see is that super 
# may be called many times over in a deep inheritance tree when calling the constructor for the deepest class.


# R-2.21
# What are some potential efficiency disadvantages of having very shallow inheritance trees, 
# that is, a large set of classes, A, B, C, and so on, such that all of these classes extend a single class, Z?

# Also, if there is a method signature that is overridden in each class, 
# the compiler will take longer to sort out or determine which method is overridden.
# So a bunch of classes extending one class becomes disorganized.


# R-2.22
# The collections.Sequence abstract base class does not provide support for comparing two sequences to each other. 
# Modify our Sequence class from Code Fragment 2.14 to include a definition for the __eq__ method, 
# so that expression seq1 == seq2 will return True precisely when the two sequences are element by element equivalent.
from abc import ABCMeta, abstractmethod    # need these definitions 

class Sequence(metaclass = ABCMeta):
	"""Our own version of collections.Sequence"""

	@abstractmethod
	def __len__(self):
		"""Return the length of the sequence."""
		pass

	@abstractmethod
	def __getitem__(self, j):
		"""Return the element at index j of the sequence."""
		pass

	def __contain__(self, val):
		"""Return True if val found in the sequence; False otherwise."""
		for j in range(len(self)):
			if self[j] == val:     # found match
				return True
			return False

	def index(self, val):
		"""Return leftmost index at which val is found(or raise ValueError)."""
		for j in range(len(self)):
			if self[j] == val:       # leftmost match
				return j 
			raise ValueError('value not in sequence')    # never found a match

	def count(self, val):
		"""Return the number of elements equal to give value."""
		k = 0
		for j in range(len(self)):
			if self[j] == val:       # found a match
				k += 1
		return k 

	def __eq__(self, other):
		"""Return True when the two sequences are element by element equivalent; False otherwise."""
		if len(self) != len(other):
			return False
		else:
			for j in range(len(self)):
				if self[j] != other[j]:
					return False
				return True


# R-2.23
# In similar spirit to the previous problem, augment the Sequence class with method __lt__, 
# to support lexicographic comparison seq1 < seq2.
from abc import ABCMeta, abstractmethod    # need these definitions 

class Sequence(metaclass = ABCMeta):
	"""Our own version of collections.Sequence"""

	@abstractmethod
	def __len__(self):
		"""Return the length of the sequence."""
		pass

	@abstractmethod
	def __getitem__(self, j):
		"""Return the element at index j of the sequence."""
		pass

	def __contain__(self, val):
		"""Return True if val found in the sequence; False otherwise."""
		for j in range(len(self)):
			if self[j] == val:     # found match
				return True
			return False

	def index(self, val):
		"""Return leftmost index at which val is found(or raise ValueError)."""
		for j in range(len(self)):
			if self[j] == val:       # leftmost match
				return j 
			raise ValueError('value not in sequence')    # never found a match

	def count(self, val):
		"""Return the number of elements equal to give value."""
		k = 0
		for j in range(len(self)):
			if self[j] == val:       # found a match
				k += 1
		return k 

	def __eq__(self, other):
		"""Return True when the two sequences are element by element equivalent; False otherwise."""
		if len(self) != len(other):
			return False
		else:
			for j in range(len(self)):
				if self[j] != other[j]:
					return False
				return True

	def __lt__(self, other):
		"""Return True when seq1 < seq2; False otherwise."""
		if len(self) != len(other):
			return False
		else:
			for j in range(len(self)):
				if self[j] >= other[j]:
					return False
				return True



# C-2.24
# Suppose you are on the design team for a new e-book reader. What are the primary classes and methods 
# that the Python software for your reader will need? You should include an inheritance diagram for this code, 
# but you do not need to write any actual code. Your software architecture should at least include ways 
# for customers to buy new books, view their list of purchased books, and read their purchased books.



# C-2.25
# Exercise R-2.12 uses the __mul__ method to support multiplying a Vector by a number, 
# while Exercise R-2.14 uses the __mul__ method to support computing a dot product of two vectors. 
# Give a single implementation of Vector.__mul__ that uses run-time type checking 
# to support both syntaxes u * v and u * k, where u and v designate vector instances and k represents a number.

# already done it in R-2.14


# C-2.26
# The SequenceIterator class of Section 2.3.4 provides what is known as a forward iterator. 
# Implement a class named ReversedSequenceIterator that serves as a reverse iterator for any Python sequence type. 
# The first call to next should return the last element of the sequence, the second call to next should 
# return the second-to-last element, and so forth.
class ReversedSequenceIterator:
	"""A reverse iterator for any Python's sequence type."""
	def __init__(self, sequence):
		"""Create a reverse iterator for the give sequence."""
		self._seq = sequence    # keep a reference to the underlying data self.
		self._k = 0    
	def __next__(self):
		"""Return the n-to-last element, or else raise StopIteration error."""
		self._k -= 1                       # advance to next index
		if abs(self._k) <= len(self._seq):
			return self._seq[self._k]      # return the data element
		else:
			return StopIteration()         # there are no more elements
	def __iter__(self):
		"""By convention, an iterator must return itself as an iterator"""
		return self 
	def print_rvs(self, n):
		"""Print next reversed n values of the sequence"""
		print(' '.join(str(next(self)) for j in range(n)))

if __name__ == '__main__':
    ReversedSequenceIterator([1, 2, 3]).print_rvs(3)	


# C-2.27
# In Section 2.3.5, we note that our version of the Range class has implicit support for iteration, 
# due to its explicit support of both __len__ and __getitem__. The class also receives implicit support of 
# the Boolean test, “k in r” for Range r. This test is evaluated based on a forward iteration 
# through the range, as evidenced by the relative quickness of the test 2 in Range(10000000) 
# versus 9999999 in Range(10000000). Provide a more efficient implementation of the __contains__ method 
# to determine whether a particular value lies within a given range. The running time of your method 
# should be independent of the length of the range.
class Range:
	"""A class that mimic's the built-in range class."""
	
	def __init__(self, start, stop = None, step = 1):
		"""Initialize a Range instance.
		Semantics is similar to built-in range class."""
		
		if step == 0:
			raise ValueError('step cannot be 0')
		if stop is None:                 # special case of range(n)
			start, stop = 0, start       # should be treated as if range(0, n)
		
		# calculate the effective length once
		self._length = max(0, (stop - start + step - 1) // step)
		
		# need knowledge of start and step (but not stop) to support __getitem__
		self._start = start 
		self._step = step

	def __len__(self):
		"""Return number of entries in the range."""
		return self._length

	def __getitem__(self, k):
		"""Return entry at index k (using standard interpretation if negative)."""
		if k < 0:
			k += len(self)  # attempt to convert negative index
		if not 0 <= k < self._length:
			raise IndexError('index out of range')
		return self._start + k * self._step

	def __contain__(self, other):
		"""Return True if a particular value lies within a given range; False otherwise."""
		if not self._start <= other <= self._stop:
			return False
		else:
			return True if (other - self._start) % self._step == 0 else False


if __name__ == '__main__':
    t1 = timeit.Timer('9999999 in Range(10000000)', 'from __main__ import Range')
    t2 = timeit.Timer('2 in Range(10000000)', 'from __main__ import Range')
    print('9999999 time consumes: ', t1.timeit(100))
    print('2 time consumes: ', t2.timeit(100))

# output:
# 9999999 time consumes:  289.21160691800014
# 2 time consumes:  0.00014432999978453154
# from the result, we can tell the time is not that good.


# C-2.28
# The PredatoryCreditCard class of Section 2.4.1 provides a process_month method 
# that models the completion of a monthly cycle. Modify the class so that once a customer has 
# made ten calls to charge in the current month, each additional call to that function results 
# in an additional $1 surcharge.
class CreditCard:
	"""docstring for CreditCard"""
	def __init__(self, customer, bank, account, credit_limit, balance = 0):
		self._customer = customer
		self._bank = bank
		self._account = account
		self._credit_limit = credit_limit
		self._balance = balance
	def get_customer(self):
		return self._customer
	def get_bank(self):
		return self._bank
	def get_account(self):
		return self._account
	def get_credit_limit(self):
		return self._credit_limit
	def get_balance(self):
		return self._balance
	def charge(self, price):
		try:
			if price + self._balance > self._credit_limit:
				return False
			else:
				self._balance += price 
				return True
		except(TypeError):
			print('Please enter numerical type.')
	def make_payment(self, amount):      
		"""Process customer payment that reduces balance."""
		try:
			self._balance -= amount
			if amount < 0:
				raise ValueError('ValueError. Negative amount.')
		except(TypeError):
			print('Please enter numerical type.')
		except ValueError as ve:
			print(ve)


class PredatoryCreditCard(CreditCard):
	"""An extension to CreditCard that compunds interest and fees."""

	def __init__(self, customer, bank, acnt, limit, apr):
		"""Create a new predatory credit card instance.
		The initial balance is 0.

		customer:  the name of the customer (e.g., John Bowman )
		bank:      the name of the bank (e.g., California Savings )
		acnt:      the acount identifier (e.g., 5391 0375 9387 5309 )
		limit:     credit limit (measured in dollars)
		apr:       annual percentage rate (e.g., 0.0825 for 8.25% APR)
		"""
		super().__init__(customer, bank, acnt, limit)     # call super constructor
		self._apr = apr
		self._k = 0

	def charge(self, price):
		"""Charge given price to the card, assuming sufficient credit limit.
		Return True if charge was processed.
		Return False and assess $5 fee if charge is denied.
		"""
		success = super().charge(price)     # call inherited method
		if not success:
			self._balance += 5              # assess penalty
		else:
			self._k += 1
			if self._k > 10:
				self._balance += 1
		return success

	def process_month(self):
		"""Assess monthly interest on outstanding balance."""
		if self._k > 10:
			monthly_fee = (self._k - 10) * 1
		if self._balance > 0:
			# if positive balance, convert APR to monthly multiplicative factor
			monthly_factor = pow(1 + self._apr, 1/12)
			self._balance *= monthly_factor	
		self._k = 0    #reset the counter at the beginning of each month
		return self._balance


if __name__ == '__main__':
	wallet = []
	wallet.append(PredatoryCreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 3000, 0.0825))
	wallet[0].charge(10)
	wallet[0].charge(100)
	wallet[0].charge(200)
	wallet[0].charge(500)
	wallet[0].charge(60)
	wallet[0].charge(190)
	wallet[0].charge(200)
	wallet[0].charge(10)
	wallet[0].charge(10)
	wallet[0].charge(10)
	wallet[0].charge(20)
	print('Balance = ', wallet[0].get_balance())
	print('fee = ', wallet[0].process_month())

	
# C-2.29
# Modify the PredatoryCreditCard class from Section 2.4.1 so that a customer is assigned 
# a minimum monthly payment, as a percentage of the balance, and so that a late fee is assessed 
# if the customer does not subsequently pay that minimum amount before the next monthly cycle.
class PredatoryCreditCard(CreditCard):
	"""An extension to CreditCard that compunds interest and fees."""

	def __init__(self, customer, bank, acnt, limit, apr, minpay = 0):
		"""Create a new predatory credit card instance.
		The initial balance is 0.

		customer:  the name of the customer (e.g., John Bowman )
		bank:      the name of the bank (e.g., California Savings )
		acnt:      the acount identifier (e.g., 5391 0375 9387 5309 )
		limit:     credit limit (measured in dollars)
		apr:       annual percentage rate (e.g., 0.0825 for 8.25% APR)
		minpay:    minimum monthly payment, default 0
		"""
		super().__init__(customer, bank, acnt, limit)     # call super constructor
		self._apr = apr
		self._minpay = minpay
		self._k = 0

	def charge(self, price):
		"""Charge given price to the card, assuming sufficient credit limit.
		Return True if charge was processed.
		Return False and assess $5 fee if charge is denied.
		"""
		success = super().charge(price)     # call inherited method
		if not success:
			self._balance += 5              # assess penalty
		else:
			self._k += 1
			if self._k > 10:
				self._balance += 1
		return success

	def process_month(self):
		"""Assess monthly interest on outstanding balance."""
		if self._k > 10:
			monthly_fee = (self._k - 10) * 1
		if self._balance > 0:
			# if positive balance, convert APR to monthly multiplicative factor
			monthly_factor = pow(1 + self._apr, 1/12)
			self._balance *= monthly_factor	
		self._k = 0    #reset the counter at the beginning of each month
		self._minpay = self._balance * 0.5      # assign 50% of balance amount as monthly minimum payment
		return self._balance

	def make_payment(self, amount):      
		"""Process customer payment that reduces balance."""
		if amount < self._minpay: 
			self._balance += 25        # assign $25 late fee
			self._balance -= amount
		else:
			self._balance -= amount


if __name__ == '__main__':
	wallet = []
	wallet.append(PredatoryCreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 3000, 0.0825, 500))
	wallet[0].charge(2000)
	print('Balance = ', wallet[0].get_balance())
	print('fee = ', wallet[0].process_month())
	wallet[0].make_payment(1000)
	print('New balance = ', wallet[0].get_balance())
	

# C-2.30
# At the close of Section 2.4.1, we suggest a model in which the CreditCard class supports 
# a nonpublic method, _set_balance(b), that could be used by subclasses to affect a change to the balance, 
# without directly accessing the _balance data member. Implement such a model, 
# revising both the CreditCard and PredatoryCreditCard classes accordingly.
class CreditCard:
	"""docstring for CreditCard"""
	def __init__(self, customer, bank, account, credit_limit, balance = 0):
		self._customer = customer
		self._bank = bank
		self._account = account
		self._credit_limit = credit_limit
		self._balance = balance

	def get_customer(self):
		return self._customer

	def get_bank(self):
		return self._bank

	def get_account(self):
		return self._account

	def get_credit_limit(self):
		return self._credit_limit

	def get_balance(self):
		return self._balance

	def charge(self, price):
		try:
			if price + self._balance > self._credit_limit:
				return False
			else:
				self._balance += price 
				return True
		except(TypeError):
			print('Please enter numerical type.')

	def make_payment(self, amount):      
		"""Process customer payment that reduces balance."""
		try:
			self._balance -= amount
			if amount < 0:
				raise ValueError('ValueError. Negative amount.')
		except(TypeError):
			print('Please enter numerical type.')
		except ValueError as ve:
			print(ve)
	def _set_balance(self, b):
		self._balance = b


class PredatoryCreditCard(CreditCard):
	"""An extension to CreditCard that compunds interest and fees."""

	def __init__(self, customer, bank, acnt, limit, apr, minpay = 0):
		"""Create a new predatory credit card instance.
		The initial balance is 0.

		customer:  the name of the customer (e.g., John Bowman )
		bank:      the name of the bank (e.g., California Savings )
		acnt:      the acount identifier (e.g., 5391 0375 9387 5309 )
		limit:     credit limit (measured in dollars)
		apr:       annual percentage rate (e.g., 0.0825 for 8.25% APR)
		minpay:    minimum monthly payment, default 0
		"""
		super().__init__(customer, bank, acnt, limit)     # call super constructor
		self._apr = apr
		self._minpay = minpay
		self._k = 0

	def charge(self, price):
		"""Charge given price to the card, assuming sufficient credit limit.
		Return True if charge was processed.
		Return False and assess $5 fee if charge is denied.
		"""
		success = super().charge(price)     # call inherited method
		if not success:
			self._balance += 5              # assess penalty
		else:
			self._k += 1
			if self._k > 10:
				self._balance += 1
		return success

	def process_month(self):
		"""Assess monthly interest on outstanding balance."""
		if self._k > 10:
			monthly_fee = (self._k - 10) * 1
		if self._balance > 0:
			# if positive balance, convert APR to monthly multiplicative factor
			monthly_factor = pow(1 + self._apr, 1/12)
			self._balance *= monthly_factor	
		self._k = 0    #reset the counter at the beginning of each month
		self._minpay = self._balance * 0.5      # assign 50% of balance amount as monthly minimum payment
		return self._balance

	def make_payment(self, amount):      
		"""Process customer payment that reduces balance."""
		if amount < self._minpay: 
			self._balance += 25        # assign $25 late fee
			self._balance -= amount
		else:
			self._balance -= amount


# c-2.31
# Write a Python class that extends the Progression class so that each value in the progression 
# is the absolute value of the difference between the previous two values. 
# You should include a constructor that accepts a pair of numbers as the first two values, 
# using 2 and 200 as the defaults.
class Progression:
	"""Iterator producing a generic progression. 
	Default iterator produces the whole numbers 0, 1, 2, ... """
	def __init__(self, start = 0):
		"""Initialize current to the first value of the progression."""
		self._current = start 
	def _advance(self):
		"""Update self._current to a new value.
		This should be overridden by a subclass to customize progression.
		By convention, if current is set to None, this designates the end of a finite progression."""
		self._current += 1
	def __next__(self):
		"""Return the next element, or else raise StopIteration error."""
		if self._current is None:        # our convention to end a progression
			raise StopIteration()
		else:
			answer = self._current       # record current value to return
			self._advance()              # advance to prepare for next time
			return answer                # return the answer
	def iter(self):
		"""By convention, an iterator must return itself as an iterator."""
		return self
	def print_progression(self, n):
		"""Print next n values of the progression."""
		print(' '.join(str(next(self)) for j in range(n)))


class AbsDifferenceProgression(Progression):
	"""Absolute value of the difference between the previous two values"""

	def __init__(self, first = 0, second = 0):
		super().__init__(first)               # start progression at first
		self._prev = abs(second - first)     # fictitious value preceding the first

	def _advance(self):
		"""Update current value by taking the absolute difference of previous two."""
		self._prev, self._current = self._current, abs(self._prev - self._current)


if __name__ == '__main__':
	print('Absolute difference progression with start 2 and 200: ')
	AbsDifferenceProgression(2, 200).print_progression(10)


# C-2.32
# Write a Python class that extends the Progression class so that each value in the progression 
# is the square root of the previous value. (Note that you can no longer represent each value with an integer.) 
# Your constructor should accept an optional parameter specifying the start value, using 65,536 as a default.
from math import sqrt
class SqrProgression(Progression):
	"""the square root of the previous value"""
	def __init__(self, start):
		super().__init__(start)

	def _advance(self):
		self._current = round(sqrt(self._current),2)

if __name__ == '__main__':
	print('square root progression with start 200: ')
	SqrProgression(200).print_progression(10)
		

# P-2.33
# Write a Python program that inputs a polynomial in standard algebraic notation and 
# outputs the first derivative of that polynomial.
def first_derivative(polynomial):
	if len(polynomial) != 3:
		raise ValueError('Check input! Value Error!')
	else:
		a = polynomial[0]
		b = polynomial[1]
		c = polynomial[2]
		a *= 2
		for i in range(3):
			if not isinstance(polynomial[i], (int,float)):
				raise ValueError('Check input! Must be int or float!')	
		print(a, '* x +', b, '= 0')

# test it
first_derivative([5,2,1])


# P-2.34
# Write a Python program that inputs a document and then outputs a barchart plot of the 
# frequencies of each alphabet character that appears in that document.
%matplotlib inline
import matplotlib.pylab as plt

class AlphabetFrequency:
	"""Plot a barchat of the frequencies of each alphabet character that appears in that document."""
	def __init__(self, filepath):
		self._filepath = filepath
		self._document = open(filepath, 'r', encoding='utf-8')
		self._read = self._document.read()

	def count_frequency(self):
		self._words = []
		for char in self._read:
			if char.isalpha():
				self._words.append(char)
		self._freq = {}
		for k in range(97, 123):
			n = 0
			for i in self._words:
				if i.lower() == chr(k):
					n += 1
					self._freq.update({chr(k): n})
		return self._freq

	def barchart(self):
		plt.bar(range(len(self._freq)), list(self._freq.values()), align='center')
		plt.xticks(range(len(self._freq)), list(self._freq.keys()))
		plt.show()


# test
if __name__ == '__main__':
	filepath1 = '/Users/houetsu/Downloads/Python/Phoenix/P-2.34.txt'
	test1 = AlphabetFrequency(filepath1)
	print(test1.count_frequency())
	test1.barchart()
		

# P-2.35
# Write a set of Python classes that can simulate an Internet application in which one party, 
# Alice, is periodically creating a set of packets that she wants to send to Bob.
# An Internet process is continually checking if Alice has any packets to send, and if so, 
# it delivers them to Bob’s computer, and Bob is periodically checking 
# if his computer has a packet from Alice, and, if so, he reads and deletes it.
class InternetApp:
	def __init__(self, second, packet = 0):
		"""I use second here to simplfy the code. 
		However, in the real world, people won't check message periodically by second.
		We can do some modification based on the situation.
		"""
		self._period = second
		self._Alice = [0] * packet
		self._Bob = []

	def __setitem__(self, j, val):
		self._Alice[j] = val

	def _SendPacket(self):
		if len(self._Alice) > 0:
			self._Bob.extend(self._Alice)
			print('Successfully send to Bob.')
			return self._Bob

	def ReadPacket(self):
		time.sleep(self._period)
		print('The packets from Alice are: ', self._Bob)
		self._Bob = []
		print('Delete what Bob read. There is no unread packet now.', self._Bob)
		

if __name__ == '__main__':
	test = InternetApp(5,3)
	test[0] = 'first packet'
	test[1] = 'second packet'
	test[2] = 'third packet'
	print(test.SendPacket())
	test.ReadPacket()


# P-2.36
# Write a Python program to simulate an ecosystem containing two types of creatures, bears and fish. 
# The ecosystem consists of a river, which is modeled as a relatively large list. 
# Each element of the list should be a Bear object, a Fish object, or None. 
# In each time step, based on a random process, each animal either attempts to move 
# into an adjacent list location or stay where it is. If two animals of the same type 
# are about to collide in the same cell, then they stay where they are, 
# but they create a new instance of that type of animal, which is placed in a random empty 
# (i.e., previously None) location in the list. If a bear and a fish collide, however, 
# then the fish dies (i.e., it disappears).

# not finish yet 

import random

class Creature:
	def __init__(self, bear = 0, fish = 0):
		self._bear = bear
		self._fish = fish
		self._list = []

	def CreateList(self):
		self._list.extend(self._bear * [1])
		# use 1 stands for bear
		self._list.extend(self._fish * [0])
		# use 0 stands for fish
		return self._list

	def __getitem__(self, j):
		return self._list[j]

	def __len__(self):
		return len(self._list)



class Ecosystem:
	def __init__(self, length, Creature, Times = 0):
		if len(Creature) > length:
			raise ValueError('No enough space!')
		else:
			self._len = length
			self._creature = list(Creature)
			none_cnt = self._len - len(self._creature)
			self._creature.extend(none_cnt *[None])
			random.shuffle(self._creature)
			self._times = Times

	def OriginalRiver(self):
		"""Return original river with bear, fish, and None"""
		self._creatureStr = []
		for val in self._creature:
			if val == 1:
				self._creatureStr.append('Bear')
			elif val == 0:
				self._creatureStr.append('Fish')
			else:
				self._creatureStr.append(None)
		print('The original ecosystem is: ', self._creatureStr) 

	def move(self):
		self._index_dict = {}  # {old index: new index}
		self._ind_list = []    # new index list
		self._SameInd = []
		for i in range(self._len):
			j = random.choice([-1,1])
			self._new_ind = i + j
			if self._new_ind == self._len:
				self._new_ind = 0
			self._ind_list.append(self._new_ind)
			self._index_dict.update({i: self._new_ind})
		return self._index_dict

	def same(self):
		for v in range(self._len):
			for w in range(self._len):
				if v != w and self._index_dict[v] == self._index_dict[w]:
					self._SameInd.append(self._index_dict[v])
		self._SameInd = list(dict.fromkeys(self._SameInd))  # remove duplicate values
		return self._SameInd  # same new index 

	def TimeStep(self):
		step = 0
		while step <= self._times:
			self.move()
			self.same()
			step += 1
			if len(self._SameInd) == 0:
				"""If there is no clide during the movement"""
				for k in range(self._len):
					m = self._index_dict[k]
					self._creature[m] = self._creature[k]
				return self._creature 
			else:
				prev_list = []
				for prev in range(len(self._index_dict)):
					if self._index_dict[prev] in self._SameInd:
						prev_list.append([prev, self._index_dict[prev]])
				for p in range(len(prev_list)):
					for q in range(len(prev_list)):
						if p != q and prev_list[p][1] == prev_list[q][1]:
							if self._creature[p] == self._creature[q]:
							


					
						 


# P-2.37
# Write a simulator, as in the previous project, but add a Boolean gender field and a floating-point 
# strength field to each animal, using an Animal class as a base class. If two animals of the same type 
# try to collide, then they only create a new instance of that type of animal if they are of
# different genders. Otherwise, if two animals of the same type and gender try to collide, 
# then only the one of larger strength survives.




			


	















