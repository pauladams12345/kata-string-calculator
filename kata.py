import unittest
import random

# Calculates the sum of a string of integers of undefined
# length. If no numbers are supplied, returns 0. Negative values
# are not allowed. Values >1000 are not added to the sum.
# Parameters:
# 	s: a string of integers. Delimiters allowed by default: ',' and '\n'
#	   Custom delimiters are allowed when the string begins as follows:
#	   '//[delimiter]\n' Example: '//;\n1;2'
# Returns:
#	Sum of supplied numbers, or 0 if input is empty. If negative values are
#	present in the input, an exception will be raised.
def add(s):
	if s[0:2] == '//':							# handle custom delimiter
		custom_delimiter = s[2]
		s = s[4:]
		s = s.replace(custom_delimiter, ',')

	s = s.replace('\n',',')				# handle '\n' delimiter
	
	if s == '':							# empty string returns 0
		return 0
	else:								# 1+ ints, split by ',' and sum
		nums = s.split(',')
		total = 0
		negatives = ''					# keep track of illegal negatives
		for num in nums:				# sum up ints, and track negatives
			if int(num) < 0:
				negatives += num + ', '
			total += int(num)
		
		if negatives != '':				# if there were any negatives, raise exeption
			negatives = negatives[:-2]	# remove trailing ', '
			raise ValueError('Negative values are not allowed. Illegal values: ' + negatives)
		else:
			return total

class TestAdd(unittest.TestCase):
	def test_empty_input(self):
		self.assertEqual(add(''), 0)

	def test_single_num(self):
		self.assertEqual(add('5'), 5)

	def test_two_nums_with_comma_separator(self):
		self.assertEqual(add('1,2'), 3)

	def test_two_nums_with_newline_separator(self):
		self.assertEqual(add('1\n2'), 3)

	def test_random_quantity_of_random_nums_with_either_separator(self):
		length = random.randint(100,10000)
		total = 0
		s = ""
		for i in range(length):
			num = random.randint(0,1000)
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

	def test_single_negative_value(self):
		with self.assertRaisesRegex(ValueError \
			, 'Negative values are not allowed. Illegal values: -1'):
			add('-1')

	def test_multiple_negative_values(self):
		with self.assertRaisesRegex(ValueError \
			, 'Negative values are not allowed. Illegal values: -4, -6, -8'):
			add('//;\n1,2\n3;-4,5,-6,7,-8')

if __name__ == '__main__':
	unittest.main()