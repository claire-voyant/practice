handle = open('numbers.txt','r')

index = 0
while True:
    line = handle.readline()
    if len(line) == 0:
        break
    fields = line.split()
    numbers = [int(x) for x in fields]
    for number in numbers:
        print number,
        if index % 10 == 9:
            print
        index += 1

if index % 10 == 9:
    print

handle.close()
