import re

input=open('C:/Users/Karla/Documents/AoC2023/Day4/test_input.txt','r').read()
lines=input.splitlines()

winning_numbers=list()
numbers=list()

def substring_after(s, delim):
    return s.partition(delim)[2]

def substring_before(s, delim):
    return s.partition(delim)[0]

def line_simplification(line):
    _, line= line.split(':') # Splits line into two part with ':' used as delimiter
    # And only right hand side of ':' is saved into line
    lhs, rhs = line.split('|')
     # If list is changed to a set. Intersection (presjek skupa) can be found.
    # set(lhs.split()) & set(rhs.split()) returns new set that consists only of
    # matching numbers
    # Only number of matches is needed so lentgth of this set is returned 
    return len(set(lhs.split()) & set(rhs.split()))

score=0
for line in lines:
    score+=int(pow(2,line_simplification(line)-1))
    line=substring_after(line, ':')
    winning_numbers.append(substring_before(line, '|'))
    numbers.append(substring_after(line, '|'))

print(score)

winners=list()
nums=list()
for winner in winning_numbers:
    winners.append(re.findall(r'\d+', winner))

for element in numbers:
    nums.append(re.findall(r'\d+', element))

matches=list()
sum_out=0
for i, num in enumerate(nums):
    counter2=0
    for j, el in enumerate(num):
        counter1=0
        while counter1 < len(winners[i]):
            # print(winners[i][counter])
            if el == winners[i][counter1]:
                counter2+=1
            counter1+=1
    matches.append(counter2)
    if counter2 >=1:
        sum_out+=pow(2,counter2-1)

print(sum_out)

# Part 2

i=0
cards=list()
while i < len(nums):
    cards.append(1)
    i+=1

for i,el in enumerate(cards):
    j=i+1
    counter=0
    counter1 = 0
    while counter1 < el:
        while counter < matches[i] & matches[i] != 0:
            cards[j]+=1
            counter+=1
            j+=1
        counter=0
        j=i+1
        counter1+=1

sum2=0
for i,el in enumerate(cards):
    sum2+=el
print(sum2)
