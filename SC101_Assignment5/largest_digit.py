"""
File: largest_digit.py
Name: 黃元品
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	# change negative number
	if n < 0:
		n = n * (-1)

	# base case
	if n < 10:
		return n

	else:
		n_largest = n % 10  # get last digit
		n = n // 10  # remove last digit
		if n_largest > find_largest_digit(n):  # recursion
			return n_largest
		else:
			return find_largest_digit(n)


if __name__ == '__main__':
	main()
