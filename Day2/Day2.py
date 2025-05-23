# Bags contain 12 red cubes, 13 green cubes, and 14 blue cubes
import re

input=open('C:/Users/Karla/Documents/Advent of Code 2023/Day2/test_input.txt','r').read()
lines=input.splitlines()

numbers=list()
digits=list()

green=list()
red=list()
blue=list()
green_game_possible=list()
red_game_possible=list()
blue_game_possible=list()

game_possible=list()
sum=0

# Variables for part 2
maximum_green=list()
maximum_red=list()
maximum_blue=list()

def substring_after(s, delim):
    return s.partition(delim)[2]

for line in lines:
    line=substring_after(line, ':')
    # numbers.append(re.findall(r'\b\d+\b', line))
    green.append(re.findall(r'\b\d+\b green', line))
    blue.append(re.findall(r'\b\d+\b blue', line))
    red.append(re.findall(r'\b\d+\b red', line))
    # digits=[char for char in line if char.isnumeric()]
    # if digits:
	#     numbers.append(digits[0]+digits[-1])

for num, element in enumerate(green):
    i=0
    flag=1
    for item in element:
        # green[num][i]= int(re.sub(' green', '', green[num][i]))
        green[num][i]= int(item.split()[0])
        if int(green[num][i]) > 13:
            flag=0
        i+=1
    if flag == 1:
        green_game_possible.append(num+1)

for num, element in enumerate(red):
    i=0
    flag=1
    for item in element:
        red[num][i]= int(re.sub(' red', '', red[num][i]))
        if int(red[num][i]) > 12:
            flag=0
        i+=1
    if flag == 1:
        red_game_possible.append(num+1)

for num, element in enumerate(blue):
    i=0
    flag=1
    for item in element:
        blue[num][i]= int(re.sub(' blue', '', blue[num][i]))
        if int(blue[num][i]) > 14:
            flag=0
        i+=1
    if flag == 1:
        blue_game_possible.append(num+1)
game_possible.append(set(green_game_possible) & set(blue_game_possible) & set(red_game_possible))
# print(game_possible)
for i in game_possible:
    for j in i:
        sum+=j
print('Part 1 answer:', sum)

# Part 2

for num, element in enumerate(green):
    max=0
    for item in element:
        if item > max:
            max=item
    maximum_green.append(max)

for num, element in enumerate(red):
    max=0
    for item in element:
        if item > max:
            max=item
    maximum_red.append(max)

for num, element in enumerate(blue):
    max=0
    for item in element:
        if item > max:
            max=item
    maximum_blue.append(max)

product=list()
for num,maximum in enumerate(maximum_green):
    product.append(maximum*maximum_blue[num]*maximum_red[num])

total=0
for i in product:
    total+=i

print('Part 2 answer:', total)




