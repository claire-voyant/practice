import sys
import random

def main():
    values = [1,2,3,4,5,6]
    probs  = [0.1, 0.2, 0.1, 0.2, 0.15, 0.25]
    mygen = biased_generator(values,probs,1000)
    for i in mygen:
      print i

def biased_generator(values, probabilities, count):
  for x in xrange(count):
    b = 0    
    cum_probs = [0,0,0,0,0,0]
    for i in range(0,len(cum_probs)):
      for j in range(0,i+1):
        cum_probs[i] += probabilities[j]
   
    r = random.random()
    index = 0
    i = 0
    for c in cum_probs:
       if r < c:
         i = index
         break
       index += 1
    yield values[i] 
   


if __name__ == '__main__':
        main()
