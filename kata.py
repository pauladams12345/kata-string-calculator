import unittest

# Calculates the sum of up to two numbers. If no
# numbers are supplied, returns 0
# Parameters:
# 	s: a string of integers separated by a comma
# Returns:
#	Sum of supplied numbers, or 0 if input is empty
def add(s):
	if s == '':
		return 0
	elif ',' not in s:
		return int(s)
	else:
		nums = s.split(',')
		num1 = int(nums[0])
		num2 = int(nums[1])
		return num1 + num2

class TestAdd(unittest.TestCase):
	def test_empty_input(self):
		self.assertEqual(add(''), 0)

	def test_single_num(self):
		self.assertEqual(add('5'), 5)
		self.assertEqual(add('-5'), -5)

	def test_two_nums(self):
		self.assertEqual(add('1,2'), 3)
		self.assertEqual(add('1,-2'), -1)

if __name__ == '__main__':
	unittest.main()