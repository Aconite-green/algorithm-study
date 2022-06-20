# Get the test scores of 5 people and find the average and sum

score1 = int(input('student number 1? :'))
score2 = int(input('student number 2? :'))
score3 = int(input('student number 3? :'))
score4 = int(input('student number 4? :'))
score5 = int(input('student number 5? :'))

total = 0
total += score1
total += score2
total += score3
total += score4
total += score5
print(f'sum is {total}')
print(f'average is {total/5}')

# Arrays are useful when the requirements below exist
#1. If you change the number of students
#2. To view or change a specific student's test scores
#3. If you need to find the lowest and highest points or sort

# Data structure: a physical or logical relationship between a data unit and the data itself