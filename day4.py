import re

file = open("day4.txt", "r")
dictionary = {}
array = []
validarray = []
counter = 0

def isvalid(dict):
    if int(dict["byr"]) >1919 and int(dict["byr"]) < 2021 and int(dict["iyr"]) > 2009 and int(dict["iyr"]) < 2021 and int(dict["eyr"]) > 2019 and int(dict["eyr"]) < 2031:
        if (dict["hgt"][-2:] == "cm" and int(dict["hgt"][:-2]) > 149 and int(dict["hgt"][:-2]) < 194) or (dict["hgt"][-2:] == "in" and int(dict["hgt"][:-2]) > 58 and int(dict["hgt"][:-2]) < 77):
            if re.search("^#[a-f0-9]{6}$", dict["hcl"]) is not None:
                if dict["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    if len(dict["pid"]) == 9:
                        return True
    return False
for line in file:
    if line != "\n":
        line = line.strip()
        line = line.split(" ")
        for element in line:
            element = element.split(":")
            dictionary[element[0]] = element[1]
    else:
        array.append(dictionary)
        dictionary = {}


for dict in array:
    if "byr" in dict and "iyr" in dict and "eyr" in dict and "hgt" in dict and "hcl" in dict and "ecl" in dict and "pid" in dict:
        validarray.append(dict)

for dict in validarray:
    if isvalid(dict):
        counter += 1

print(counter)

str = "hello"
print(str[:-2])
