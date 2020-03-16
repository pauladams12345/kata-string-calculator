import unittest
import random

# Calculates the sum of a string of integers of undefined
# length. If no numbers are supplied, returns 0
# Parameters:
# 	s: a string of integers. Delimiters allowed by default: ',' and '\n'
#	   Custom delimiters are allowed when the string begins as follows:
#	   '//[delimiter]\n' Example: '//;\n1;2'
# Returns:
#	Sum of supplied numbers, or 0 if input is empty
def add(s):
	if s[0:2] == '//':							# handle custom delimiter
		custom_delimiter = s[2]
		s = s[4:]
		s = s.replace(custom_delimiter, ',')

	s = s.replace('\n',',')						# handle '\n' delimiter
	
	if s == '':									# empty string returns 0
		return 0
	elif ',' not in s:							# single int
		return int(s)
	else:										# multiple ints, split by ',' and sum
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

	def test_custom_delimiter_only(self):
		self.assertEqual(add('//;\n1;2;3'), 6)
		self.assertEqual(add('//$\n1$2'), 3)

	def test_custom_and_default_delimiters(self):
		self.assertEqual(add('//;\n1,2\n3;4'), 10)

if __name__ == '__main__':
	unittest.main()