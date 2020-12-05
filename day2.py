file = open("day2.txt", "r")
array = []
counter = 0
for line in file:
    line = line.strip()
    line = line.split(" ")
    array.append(line)

for element in array:
    if element[3].count(element[2]) >= int(element[0]) and element[3].count(element[2]) <= int(element[1]):
        counter += 1

print(counter)
counter = 0

for element in array:
    if element[3][int(element[0])-1]  == element[2] and element[3][int(element[1])-1]  != element[2]:
        counter += 1
    elif element[3][int(element[1])-1]  == element[2] and element[3][int(element[0])-1]  != element[2]:
        counter += 1

print(counter)
