import re

numbers_fwd=list()
numbers_bwd=list()
numbers=list()
numeric_line=''
numeric_lines=list()
numeric_lines_filter=list()
sum=0
sum2=0

numwords = ['zero','one','two','three','four','five','six','seven','eight','nine']
num_non_num_words = ['0','1','2','3','4','5','6','7','8','9','zero','one','two','three','four','five','six','seven','eight','nine']
numeric_words=list()

word_digit_pairs = [
    ('zero', '0'),
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9')
]

input=open('C:/Users/Karla/Documents/AoC2023/Day1/test_input.txt','r').read()
lines=input.splitlines()

# Part 1

for line in lines:
    i=0
    j=0
    for char in line:
        if char.isdigit():
            numbers_fwd.append(int(char))
            i+=1
        if i==1:
            break
        else:
            continue
    for char in reversed(line):
        if char.isdigit():
            numbers_bwd.append(int(char))
            j+=1
        if j==1:
            break
        else:
            continue


numbers = [(x*10) + y for x, y in zip(numbers_fwd, numbers_bwd)]

for element in numbers:
    sum+=element

print ('Sum Part1:', sum)

# Part 2
numwords={}

for line in lines:
    numeric_line=line
    for word, digit in word_digit_pairs:
        if word == 'two' and re.search(r'eightwo', numeric_line):
            numeric_line = numeric_line.replace('eight', '8t')
        if word == 'three' and re.search(r'eighthree', numeric_line):
            numeric_line = numeric_line.replace('eight', '8t')
        if word == 'eight' and re.search(r'nineight', numeric_line):
            numeric_line = numeric_line.replace('nine', '9e')
        if word == 'one' and re.search(r'twone', numeric_line):
            numeric_line = numeric_line.replace('two', '2o')
        if word == 'one' and re.search(r'oneight', numeric_line):
            numeric_line = numeric_line.replace('one', '1e')
        if word == 'five' and re.search(r'fiveight', numeric_line):
            numeric_line = numeric_line.replace('five', '5e')
        if word == 'three' and re.search(r'threeight', numeric_line):
            numeric_line = numeric_line.replace('three', '3e')
        if word == 'one' and re.search(r'oneight', numeric_line):
            numeric_line = numeric_line.replace('one', '1e')
        if word == 'zero' and re.search(r'zerone', numeric_line):
            numeric_line = numeric_line.replace('zero', '0e')
        else:
            numeric_line = numeric_line.replace(word, digit)
    numeric_lines.append(numeric_line)

# print('Numeric lines: ', numeric_lines)

for line in numeric_lines:
    numeric_line=line
    for word, digit in word_digit_pairs:
        numeric_line = numeric_line.replace(word, digit)
    numeric_lines_filter.append(numeric_line)

# print('Numeric lines filter: ', numeric_lines_filter)

for line in numeric_lines:
    i=0
    j=0
    for char in line:
        if char.isdigit():
            numbers_fwd.append(int(char))
            i+=1
        if i==1:
            break
        else:
            continue
    for char in reversed(line):
        if char.isdigit():
            numbers_bwd.append(int(char))
            j+=1
        if j==1:
            break
        else:
            continue


numbers = [(x*10) + y for x, y in zip(numbers_fwd, numbers_bwd)]

for element in numbers:
    sum2+=element

print ('Sum Part2:', sum2)

            
