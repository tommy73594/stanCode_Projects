"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""


def main():
# 宣告變數
    cla = []
    sc001 = []
    sc101 = []
    count_001 = 0
    count_101 = 0
    total_001 = 0
    total_101 = 0
    max_value_sc001 = None
    min_value_sc001 = None
    max_value_sc101 = None
    min_value_sc101 = None
    
# 判斷輸入並儲存
    while cla != '-1':
        cla = input('Which class? ')
        cla = cla.lower()
        if cla == '-1': break
    
        score = input('Score: ')
        score = int(score)

        if cla == 'sc001':
            sc001.append(score)
        elif cla == 'sc101':
            sc101.append(score)

#判斷大小值與計算總和
    for score in sc001:
        count_001 +=1
        total_001 += score
        if(max_value_sc001 is None or score > max_value_sc001):
            max_value_sc001 = score
        if(min_value_sc001 is None or score < min_value_sc001):
            min_value_sc001 = score

    for score in sc101:
        count_101 +=1
        total_101 += score
        if(max_value_sc101 is None or score > max_value_sc101):
            max_value_sc101 = score
        if(min_value_sc101 is None or score < min_value_sc101):
            min_value_sc101 = score


#判斷是否有輸入，計算平均值與輸出   
    if count_001 > 0 or count_101 > 0:
        if count_001 > 0:
            avg_value_001 = float(total_001 / count_001)
            print('==============SC001==================')
            print('MAX (001): ', max_value_sc001)
            print('Min (001): ', min_value_sc001)
            print('Avg (001): ', avg_value_001)

        else:
            print('==============SC001==================')
            print('No score for SC001')

        if count_101 > 0: 
            avg_value_101 = float(total_101 / count_101)
            print('==============SC101==================')
            print('MAX (101): ', max_value_sc101)
            print('Min (101): ', min_value_sc101)
            print('Avg (101): ', avg_value_101)
        else:
            print('==============SC101==================')
            print('No score for SC101')
    else:
        print('No class scores were entered')


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
