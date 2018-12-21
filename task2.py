input_file = 'ukraine_deputies.csv'
import re

def getName(line):
    list = line.split(",")
    name = list[3]
    real = r'\w+ \w+ \w+'
    if (not re.match(real, name)):
        return name
    else:
        for i in range(len(name)):
            word = name[i]
            word[0].upper() + word[1:].lower()
            return name

def getParty(line):
    list = line.split(",")
    party = list[4]
    real = r'\w+'
    if (not re.match(real, party)):
        return "-"
    else:
        return party.lower()

def getCity(line):
    list = line.split(",")
    city = list[5]
    real = r'\w+'
    if (not re.match(real, city)):
        return " "
    else:
        return city[0].upper() + city[1:].lower()

def getConstituency(line):
    list = line.split(",")
    constituency = list[6]
    real = r'\w+'
    if (not re.match(real, constituency)):
        return " "
    else:
        return constituency[0].upper() + constituency[1:].lower()


try:
   with open(input_file, encoding="utf-8", mode='r') as file:
       file.readline()

       line_number = 1
       for line in file:
           line = line.strip().rstrip()
           line_number += 1
           if line_number > 100:
               break
           if not line:
               continue

           name = getName(line)
           party = getParty(line)
           city = getCity(line)
           constituency = getConstituency(line)

           print(name,", ", party,", ", city,", ", constituency)



except IOError as e:
   print ("I/O error({0}): {1}".format(e.errno, e.strerror))

except ValueError as ve:
    print("Value error {0} in line {1}".format(ve, line_number))
