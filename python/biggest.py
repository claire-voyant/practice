import sys
myFile = sys.argv[1:]

handle = open(str(myFile[0]), 'r')
first_time = True

numbers = []
while True:
    line = handle.readline()
    if len(line) == 0:
        break
    fields = line.split()
    for field in fields:
        numbers.append(float(field))

count = 0.0
mean = 0.0


for num in numbers:
 mean += float(num)
 count += 1.0

mean = mean / count
s2 = 0.0
for num in numbers:
  temp = (float(num) - mean)**2
  s2 += temp

stDev = (s2 / (count -1)) ** 0.5

median = 0.0
indexMedian = count / 2
if count % 2 == 0:
  median = (numbers[int(indexMedian)] + numbers[int(indexMedian)+1]) /2
else:
  median = numbers[indexMedian]

    
file.close(handle)
print "mean: " + str(mean)
print "std dev: " + str(stDev)
print "median: " + str(median)
 
