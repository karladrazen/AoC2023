import re


def translate(line):
	for num, name in enumerate(digit_names):
		line = line.replace(name, f"{name}{num}{name}")
	return line
digit_names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

input=open('C:/Users/Karla/Documents/Advent of Code 2023/test_input.txt','r').read()

lines = input.splitlines()

# Define new function, it gets string as input
def translate(line):
	for num, name in enumerate(digit_names):
		line=line.replace(name, name + str(num) + name)
		print(line)
		# line=line.replace(name, f"{name}{num}{name}")
	return line

sum1=0
sum2=0
for line in lines:
	digits=[char for char in line if char.isnumeric()]
	if digits:
		sum1+=int(digits[0]+digits[-1])
	
	digits=[char for char in translate(line) if char.isnumeric()]
	sum2+=int(digits[0]+digits[-1])
print(sum1)
print(sum2)
# total1 = 0
# total2 = 0
# for line in lines:
# 		# digits = []
# 		# for char in line:
# 		# 	if char.isnumeric():
# 		# 		digits.append(char)
# 		digits = [char for char in line if char.isnumeric()]
# 		if digits:
# 			total1 += int(digits[0]+digits[-1])

# 		digits = [char for char in translate(line) if char.isnumeric()]
# 		total2 += int(digits[0]+digits[-1])
# print('Total1', total1)
# print('Total2', total2)


