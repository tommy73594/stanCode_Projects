"""
File: anagram.py
Name: 黃元品
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
words = []


def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        read_dictionary()
        ans = find_anagrams(s)
        print(str(len(ans)) + ' anagrams: ' + str(ans))


def read_dictionary():
    global words
    with open(FILE, 'r') as f:
        for word in f:
            word = word.strip()
            words.append(word)


def find_anagrams(s):
    """
    :param s: the word for anagram
    :return ans: all anagram
    """
    ans = []
    print('Searching...')
    find_anagrams_helper(s, '', ans)
    return ans


def find_anagrams_helper(s, current, ans):
    if len(s) == 0:  # base case
        if current in words and current not in ans:
            print('Found:  '+current)
            print('Searching...')
            ans.append(current)
    else:
        for i in range(len(s)):
            # Choose
            other_s = s[:i] + s[i + 1:len(s)]  # remove used letter
            current += s[i]
            # Explore
            if has_prefix(current):
                find_anagrams_helper(other_s, current, ans)
            # Un-choose
            current = current[:-1]


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for word in words:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
