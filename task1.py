input_file = 'ukraine_deputies.csv'
try:
   with open(input_file, encoding="utf-8", mode='r') as file:
       file.readline()

       line_number = 1
       for line in file:
           line = line.strip().rstrip()
           line_number += 1
           if line_number > 20:
               break
           print(line)
           if not line:
               continue

except IOError as e:
   print ("I/O error({0}): {1}".format(e.errno, e.strerror))

except ValueError as ve:
    print("Value error {0} in line {1}".format(ve, line_number))
# город сколько партий столбик
#сколько городов крутовая
#сколько разных партий круг