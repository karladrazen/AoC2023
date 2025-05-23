import re

input=open('C:/Users/Karla/Documents/AoC2023/Day3/test_input.txt','r').read()
lines=input.splitlines()

part_number=list()
position=list()


for i,line in enumerate(lines):
    part_number.append(re.findall(r'\d+', line))


for i,line in enumerate(lines):
    position.append([(x.start(), x.end()-1, i) for x in re.finditer(r'\d+', line)])

sum=0
for i,row in enumerate(position):
    for index, j in enumerate(row):
        # row is tuple list
        # print('j-th element in i-th row is: \n', j)
        # j is individual tuple
        
        double_flag=0 # flag introduced to avoid double summation
        tuple_start=j[0]
        tuple_end=j[1]
        x_coordinate=j[2]
        if row != []:
            if tuple_start != 0 and tuple_end != 139:
                if lines[i][tuple_start-1] != '.' or lines[i][tuple_end+1] != '.' and double_flag==0:
                    double_flag=1
                    sum+=int(part_number[i][index])
                    
            elif tuple_start == 0:
                if lines[i][tuple_end+1] != '.' and double_flag==0:
                    double_flag=1
                    sum+=int(part_number[i][index])
                    

            elif tuple_end == 139:
                if (lines[i][tuple_start-1] != '.' or lines[i-1][tuple_start-1] != '.') and double_flag==0:
                    double_flag=1
                    sum+=int(part_number[i][index])
                    

            if i <= len(lines)-2 and i != 0 and double_flag==0 and tuple_end != 139:
                while (tuple_start-1)<(tuple_end+1):
                    if ((lines[i+1][tuple_start-1] != '.' or lines[i+1][tuple_start] != '.') and double_flag==0):
                        sum+=int(part_number[i][index])
                        double_flag=1
                        break                
                    elif ((lines[i-1][tuple_start-1] != '.' or lines[i-1][tuple_start] != '.' or lines[i-1][tuple_end+1] != '.') and double_flag==0):
                        sum+=int(part_number[i][index])
                        double_flag=1
                        break    
                    else:
                        tuple_start+=1
            elif i == 0:
                while (tuple_start-1)<(tuple_end+1):
                    if ((lines[i+1][tuple_start-1] != '.' or lines[i+1][tuple_start] != '.' or lines[i+1][tuple_end+1] != '.') and double_flag==0):
                        sum+=int(part_number[i][index])
                        double_flag=1
                        break
                    else:
                        tuple_start+=1
            elif i == (len(lines)-1):
                while (tuple_start-1)<(tuple_end+1):
                    if ((lines[i-1][tuple_start-1] != '.') and double_flag==0):
                        sum+=int(part_number[i][index])
                        double_flag=1
                        break    
                    else:
                        tuple_start+=1
                
print('Sum is {s}\n'.format(s=sum))

# Part 2
P = complex
j = complex(0,1)
adj = [P(-1,1), P(0,1),  P(1,1),
		P(-1,0), 		 P(1,0),
		P(-1,-1), P(0,-1), P(1,-1)]

grid={}
coordinates=[]
parts_list=list()
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        grid[P(x,y)] = char
        if char == '*':
            coordinates.append(P(x,y))
product=0
for i,coordinate in enumerate(coordinates):
    parts = set()
    for d in adj:
        pos= coordinate+d
        if pos not in grid or not grid[pos].isnumeric():
            num=''
        # print('Element is: {el}, my position is {pos} for {i}-th *'.format(el=grid[pos-j],pos=pos-j,i=i))
        elif pos in grid and grid[pos].isnumeric():
            num=''
            while pos-j in grid and grid[pos-j].isnumeric():
                pos -= j
            while pos in grid and grid[pos].isnumeric():
                num+=grid[pos]
                pos+=j
        if num != '':
            parts.add(int(num))
    parts_list=list(parts)
    if len(parts) == 2:
        product += parts_list[0]*parts_list[1]
        # print('Element list is {el}'.format(el=parts))
        
print('Sum of products is {product}'.format(product=product))