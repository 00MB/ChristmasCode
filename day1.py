#If anyone reads this, idc that my code is horrible, just trying to find a certain number :)

file = open("day1.txt", "r")
array = []
for x in file:
    x = int(x.strip())
    array.append(x)
print(array)
answer = 0

for x in range(len(array)):
    for y in range(x, len(array)):
        if array[x] + array[y] == 2020:
            print("yes")
            answer = array[x] * array[y]

print(answer)

for x in range(len(array)):
    for y in range(x, len(array)):
        for z in range(y, len(array)):
            if array[x] + array[y] + array[z] == 2020:
                print("yes")
                answer = array[x] * array[y] * array[z]

print(answer)
