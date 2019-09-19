# R-1.1
def is_multiple(n,m):
	if int(n) % int(m) == 0:
		return True
	else:
		return False
n = input('n = ')
m = input('m = ')
is_multiple(n,m)


# R-1.2
def is_even(k):
	if int(k) % 2 == 0:
		return True
	else:
		return False
k = input('k = ')
is_even(k)


# R-1.3
def minmax(data):
	minimum = data[0]
	maximum = data[0]
	for i in data:
		if i < minimum:
			minimum = i 
		elif i > maximum:
			maximum = i 
		else:
			minimum = i 
			maximum = i 
	return minimum, maximum


# R-1.4
def sumofsquare(n):
    n = int(input('input a positive integer: '))
    q = 0
    for i in range(1,n):
        k = n-i
        q = k*k + q
    print(q) 
sumofsquare(n)


# R-1.5
n = int(input('input a positive integer: '))
sumofsquares = sum([(n-i)*(n-i) for i in range(1,n)])
print(sumofsquares)


# R-1.6
n = int(input('input a positive integer: '))
k = 1
s = 0
while k < n:	
	s = s + k
	k = k + 2
print(s)


# R-1.7
n = int(input('input a positive integer: '))
s = sum([2*k-1 for k in range(1, n//2+1)])
print(s)


# R-1.8
n = [1, 2, 3, 4, 5, 6]
k = -2
print('n[k]: ', n[k])

j = k + len(n) # should return 3
print('n[j]: ', n[j]) #should print same value as n[k]


# R-1.9
new_range = [i*10 for i in range(5, 9)]
print(new_range)

easy_method = [i1 for i1 in range(50,90,10)]
print(easy_method)


# R-1.10
new_range = sorted([i*2 for i in range(-4, 5)], reverse = True)
print(new_range)

easy_method = sorted([i1 for i1 in range(-8,10,2)], reverse = True)
print(easy_method)


# R-1.11
m = [2**i for i in range(0,9)]
print(m)


# R-1.12
import random
q = [1,2,3,4,5]
p = 'doremifa'
k = ['do', 're', 'mi', 'fa']
choice_q = q[random.randrange(len(q))]
choice_p = p[random.randrange(len(p))]
choice_k = k[random.randrange(len(k))]
print(choice_q)
print(choice_p)
print(choice_k)


# C-1.13
n = [1, 2, 3, 4, 5]
rvs_n = []
for i in range(1,len(n)+1):
	rvs_n.append(n[len(n)-i])
print(rvs_n)
print(n)

# define a function
def reverse_list(org_list):
	rvs_n = []
	for i in range(1,len(org_list)+1):
		rvs_n.append(n[len(n)-i])
	print(rvs_n)


# C-1.14
n = [1, 2, 3, 4, 5, 6]
m = []
for i in range(0, len(n)):
	for v in range(0, len(n)):
		k = n[i] * n[v]
		if is_even(k) is False:
			m.append([n[i], n[v]])
print(m)
# is_even is the function defined in R-1.2

# define function
def odd_product_pair(data):
	m = []
	for i in range(0, len(n)):
		for v in range(0, len(n)):
			k = n[i] * n[v]
			if is_even(k) is False:
				m.append([n[i], n[v]])
	print(m)


# C-1.15
n = [1, 2, 3, 4, 5, 6]
m = [2, 4, 5, 6, 4]
s = 0
for i in range(0, len(m)):
	for v in range(0, len(m)):
		k = m[i] - m[v]
		if i != v and k == 0:
			s = s +1
if s > 0:
    print('not_distinct')
else:
    print('distinct')

# define function
def is_distinct(data):
	s = 0
	for i in range(0, len(data)):
		for v in range(0, len(data)):
			k = data[i] - data[v]
			if i != v and k == 0:
				s = s +1
	if s > 0:
		print('not_distinct')
	else:
		print('distinct')


# C-1.18
k = 0
s = [0,]
for i in range(2,20,2):
	k = k + i 
	s.append(k)
print(s)

# another method
print([k * (k - 1) for k in range(1, 11)])


# C-1.19
print([chr(k) for k in range(97, 123)])
# chr() is a built-in function in PHP and is used to convert a ASCII value to a character.


# C-1.20
def own_shuffle(data):
	new_list = []
	for i in range(0,len(data)):
		k = n[randint(0, len(n)-1)]
		new_list.append(k)
		data.remove(k)
	print(new_list)
n = [10,20,30,40,50]
own_shuffle(n)




# C-1.22
def dot_product(a,b):
	c = dict()
	for i in range(0, len(a)):
		k = {i: a[i] * b[i]}
		c.update(k)
	return c	
a1 = [5,6,7,8]
b1 = [10,20,30,40]
dot_product(a1,b1)
dot_product(a1,b1)[0]



# C-1.24
def count_vowels(string):
	vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'w']
	k = 0
	for i in range(0, len(string)):
		if string[i] in vowels:
			k = k + 1
	return k 
test_str = 'hello'
count_vowels(test_str)


# C-1.25
import string
def remove_punctuation(sentence):
    result = ''
    for i in sentence:
        if i not in string.punctuation:
            result += i
    return result
test_str = 'hello, and hoe?.d:'
remove_punctuation(test_str)


# C-1.26
a = int(input('please enter an integer: '))
b = int(input('please enter an integer: '))
c = int(input('please enter an integer: '))
def is_formula(a,b,c):
	if a + b == c:
		print('a+b=c')
	elif b - c == a:
		print('a = b - c')
	elif a * b == c:
		print('a * b = c')
	else:
		print("can't be used")


# C-1.28
def norm(v,p = None):
	if p is None:
		p = 2
	s = 0
	for i in range(0, len(v)):
		s = v[i] ** p + s
	return s

v1 = [1,2,3,4,5]
norm(v1)


# P-1.29
import itertools
def chrs_order(chrs):
    words = []
    for i in range(2, len(chrs) + 1):
        k = list(itertools.permutations(chrs,i))
        for m in range(0, len(k)):
            k1 = remove_punctuation(k[m])   # remove_punctuation() is the function we defined previously
            words.append(k1)
    print(words)

chrs1 = ['c', 'a', 't', 'd', 'o', 'g']
chrs_order(chrs1)


# P-1.30
number = int(input('Please enter an integer greater than 2: '))
def divd_2(number):
	times = 0
	while number >= 2:
		number = number/2
		times = times + 1
	return times

divd_2(9)


# P-1.31
m_charged = float(input('Please enter the monetary amount charged: '))
m_given = float(input('Please enter the monetary amount given: '))
def make_change(money_charged, money_given):
	total_change = round(money_given - money_charged, 2)
	print('Change is ' + str(total_change))
	dollar = round(total_change, 0)

	if dollar >= 100:
		hundred_dollars = round(dollar/100)
	else:
		hundred_dollars = 0
	
	str_change = str(total_change)
	ten_digits = int(str_change[-5])
	single_digits = int(str_change[-4])
	decimals = int(str_change[-2:])

	fifty_dollars = ten_digits // 5
	twenty_dollars = (ten_digits - fifty_dollars) // 2
	ten_dollars = ten_digits - fifty_dollars - twenty_dollars

	five_dollars = single_digits // 5
	one_dollars = single_digits - five_dollars

	quarters = decimals // 25
	dime = (decimals - quarters * 25) // 10
	five_cents = (decimals - quarters * 25 - dime * 10) // 5
	one_cent = decimals - quarters * 25 - dime * 10 - five_cents * 5

	print('Give back\n' + str(hundred_dollars) + ' $100 bill(s)\n' + str(fifty_dollars) + ' $50 bill\n' +
		str(twenty_dollars) + ' $20 bill(s)\n' + str(ten_dollars) + ' $10 bill(s)\n' +
		str(five_dollars) + ' $5 bill\n' + str(one_dollars) + ' $1 bill(s)\n' + str(quarters) + ' 25 cent coin(s)\n' 
		+ str(dime) + ' dime(s)\n' + str(five_cents) + ' five cents coin(s)\n' + str(one_cent) + ' one cent coin(s)')

make_change(m_charged, m_given)


# the easier method extract from the above code
def make_change(money_charged, money_given):
	total_change = round(money_given - money_charged, 2)*100
	print('Change is ' + str(total_change/100))
	amount = []
	value_list = [10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1]
	for i in range(0, len(value_list)):
		changed_value = int(total_change // value_list[i])
		total_change = total_change - changed_value * value_list[i]
		amount.append(changed_value)
	bills = ['$100 bill', '$50 bill', '$20 bill', '$10 bill', '$5 bill', '$1 bill', 
	'quarter', 'dime', '5 cent coin', '1 cent coin']
	changes = dict(zip(bills, amount))
	for key, value in changes.items():
		print(str(key) + ": " + str(value))

m_charged = float(input('Please enter the monetary amount charged: '))
m_given = float(input('Please enter the monetary amount given: '))
make_change(m_charged, m_given)















