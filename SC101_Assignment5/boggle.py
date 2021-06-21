"""
File: boggle.py
Name: 黃元品
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
words = []                   # store all possible word


def main():
	"""
	TODO:
	"""
	read_dictionary()
	letters = []
	for i in range(4):
		row_letter = input(str(i+1) + ' row of letters: ').strip()
		if len(row_letter) == 7:
			row_letter = row_letter.split(' ')
			if len(row_letter) == 4:  # check it only contain 4 letter
				letters.append(row_letter)
			else:
				print('Illegal input')
				break
		else:
			print('Illegal input')
			break
	if len(letters) == 4: 
		boggle(letters)


def boggle(letters):
	ans = []
	for i in range(0, 4):  # loop for all letter
		for j in range(0, 4):
			boggle_helper(letters, i, j, 0, 0, '', ans)
	print(f'There are {len(ans)} words in total.')


def boggle_helper(letters, row, col, pre_x, pre_y, current, ans):
	path = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (0, 1), (-1, 0), (0, -1)]  # all possible direction
	if row not in range(0, 4) or col not in range(0, 4):  # exceed the range
		return
	if len(current) > 3 and current in words:  # find the word
		if current not in ans:
			ans.append(current)
			print(f'Found "{current}"')
	current = current + letters[row][col]
	if has_prefix(current):
		for (dx, dy) in path:
			if pre_x == -dx and pre_y == -dy:  # avoid return to previous letter
				continue
			boggle_helper(letters, row+dx, col+dy, dx, dy, current, ans)
	current = current[:-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global words
	with open(FILE, 'r') as f:
		for word in f:
			word = word.strip()
			words.append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in words:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
