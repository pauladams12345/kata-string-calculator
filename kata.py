import unittest
import random

# Calculates the sum of a string of integers of undefined
# length. If no numbers are supplied, returns 0
# Parameters:
# 	s: a string of integers separated by a comma or newline (\n)
# Returns:
#	Sum of supplied numbers, or 0 if input is empty
def add(s):
	s = s.replace('\n',',')

	if s == '':
		return 0
	elif ',' not in s:
		return int(s)
	else:
		nums = s.split(',')
		total = 0
		for num in nums:
			total += int(num)
		return total

class TestAdd(unittest.TestCase):
	def test_empty_input(self):
		self.assertEqual(add(''), 0)

	def test_single_num(self):
		self.assertEqual(add('5'), 5)
		self.assertEqual(add('-5'), -5)

	def test_two_nums_with_comma_separator(self):
		self.assertEqual(add('1,2'), 3)
		self.assertEqual(add('1,-2'), -1)

	def test_two_nums_with_newline_separator(self):
		self.assertEqual(add('1\n2'), 3)

	def test_random_quantity_of_random_nums_with_either_separator(self):
		length = random.randint(100,10000)
		total = 0
		s = ""
		for i in range(length):
			num = random.randint(-1000,1000)
			total += num
			s += str(num)
			if i != length - 1:
				if num % 2 == 0:
					s += ","
				else:
					s += "\n"
		self.assertEqual(add(s), total)

if __name__ == '__main__':
	unittest.main()