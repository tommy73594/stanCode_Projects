"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r


def main():


#宣告變數
#count ＝ 用來記錄已重複的數量
#temp ＝ 暫存上次輸入的符號
#repeat ＝ 判斷是否為連續相同輸入


	count = 0
	temp = None
	repeat = False

# 輸入
	print('Let\'s flip a coin!')
	num_run = input('Number of runs: ')
	num_run = int(num_run)

#開始擲印幣直到到達連續數目
	while count != num_run:

		random = r.choice(['H','T'])

#如果為首次擲，存入暫存
		if temp == None:
			temp = random
#擲出不同時更改暫存值
		elif random != temp:
			temp = random
			repeat = False
#判斷是否重複且非連續
		elif random == temp and repeat == False:
			count = count + 1
			repeat = True
	
#印出符號
		print(random, end = '')

	print(' ')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
