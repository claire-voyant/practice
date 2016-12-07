import sys

handle = open('numbers.txt','r')
index = 0
while True:
    line = handle.readline()
    if len(line) == 0:
        break
    fields = line.split()
    numbers = [int(x) for x in fields]
    for number in numbers:
        sys.stdout.write('{:>4}'.format(number))
        if index % 10 == 9:
          print
        index += 1

if index % 10 == 9:
  print

handle.close()
