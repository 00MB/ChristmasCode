file = open("day3.txt", "r")
position = 0
trees = 0

for line in file:
    if position < (len(line) - 1):
        if line[position] == "#":
            trees += 1
    else:
        position -= (len(line) - 1)
        if line[position] == "#":
            trees += 1
    position += 7
print(trees)


position = 0
trees = 0
with open("day3.txt", "r") as file:
    count = 0
    for line in file:
        count += 1
        if count % 2 != 0:
            if position < (len(line) - 1):
                if line[position] == "#":
                    trees += 1
            else:
                position -= (len(line) - 1)
                if line[position] == "#":
                    trees += 1
            position += 1
print(trees)


250
55
54
55
39
