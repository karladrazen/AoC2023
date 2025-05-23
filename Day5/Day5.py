
input=open('C:/Users/Karla/Documents/Advent of Code 2023/Day5/short_test_input.txt','r').read()
lines=input.splitlines()
# print('Lines are:{l}\n'.format(l=lines))
numerical_codes=list()
seed_soil=list()
soil_fert=list()
fert_water=list()
water_light=list()
light_temp=list()
temp_humid=list()
humid_loc=list()

# Function used to remove word 'map' first line of each mapping
def remove_string(line):
    line, _= line.split(' ') 
    return line

def substring_split(s, delim):
    return (s.partition(delim)[0],s.partition(delim)[2])

cntr=0 # counter used as flag to split subcategories (seed-soil --> cntr=1; soil-fertilizer --> cntr=2 etc.)
# In if condition inside for loop starts from cntr+1 because the first emty line is before line: seed-to-soil map
for i,line in enumerate(lines):
    # print('{i}-th line is:{l}\n'.format(i=i,l=line))
    if line == '':
        print('This is an empty line:{l}\n'.format(l=line))
        print('Next line is map explanation: {map}\n'.format(map=lines[i+1]))
        lines[i+1]=remove_string(lines[i+1])
        print(substring_split(lines[i+1],'-to-'))
        j=0
        while lines[i+j+2] != '':
            numerical_codes.append(lines[i+j+2])
            if cntr == 0:
                seed_soil.append(lines[i+j+2])
            if cntr == 1:
                soil_fert.append(lines[i+j+2])
            if cntr == 2:
                fert_water.append(lines[i+j+2])
            if cntr == 3:
                water_light.append(lines[i+j+2])
            if cntr == 4:
                light_temp.append(lines[i+j+2])
            if cntr == 5:
                temp_humid.append(lines[i+j+2])
            if cntr == 6:
                humid_loc.append(lines[i+j+2])
            j+=1
            if i+j+2 >= len(lines):
                # humid_loc=list().append(lines[i+j])
                # print("Last line is {ll}".format(ll=lines[i+j+1]))
                break
        cntr+=1

i=0
humid_loc_num=list()
for i,el in enumerate(humid_loc):
    # num=substring_split(el, ' ')
    # print(num)
    cntr=0
    for j,num in enumerate(el):
        print(num.isdigit())
        while num.isdigit() and cntr == j:
            humid_loc_num.append(num)
        cntr+=1
    #     if num.isdigit():
    #         print(num)
# for i in range(len(humid_loc)):
#     print (i) 
# print('Only numerical values are: {num}\n'.format(num=numerical_codes))
print('Seed-soil codes are: {ss}\n'.format(ss=seed_soil))
print('Water-light codes are: {wl}\n'.format(wl=water_light))
print('Temperature-humidity codes are: {th}\n'.format(th=temp_humid))
print('Humidity-location codes are: {hl}\n'.format(hl=humid_loc))
print('Numerical Humidity-location codes are: {hln}\n'.format(hln=humid_loc_num))
# print('Single element of list field is: {el}\n'.format(el=humid_loc[1][0]))