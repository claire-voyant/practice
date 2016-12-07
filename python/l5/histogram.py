
import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()
split_lines = [line.split() for line in lines]
numbers = []
for line in split_lines:
  for number in line:
    numbers.append(float(number))
maxi = max(numbers)
mini = min(numbers)
n_bins = int(sys.argv[2])
histogram = [0 for x in range(0,n_bins)]

for number in numbers:
  bini = int((number-mini) / (maxi-mini) * n_bins)
  if bini is len(histogram):
    bini = bini -1
  histogram[bini] += 1

file.close()

print histogram
