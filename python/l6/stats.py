import math
def order(a_list, k):
    a_list.sort()
    return a_list[k]

def median(a_list):
    a_list.sort()
    length = len(a_list)
    if length % 2 == 0:
      return a_list[length/2]
    return a_list[int(length/2 + 1)]

def mode(a_list):
    myMode = {}
    for a in a_list:
      if str(a) in myMode.keys():
        myMode[str(a)] += 1
      else:
        myMode.update({str(a):1})
    maxi = 0
    maxB = 0
    for b in a_list:
      if maxi < myMode[str(b)]:
        maxi = myMode[str(b)]
        maxB = b
    return maxB 

def mean(a_list):
    num = 0.0
    total = 0.0
    for a in a_list:
      num += 1.0
      total += a 
    return float(total/num)

def variance(a_list):
    sumi = 0
    n = len(a_list)
    for a in a_list:
      sumi += (a - mean(a_list))*(a - mean(a_list))

    vari = sumi / n
    return vari

def stdev(a_list):
    return math.sqrt(variance(a_list))

def main():
    '''
    write code here to test all your functions
    '''
    l = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3]
    print mean(l)
    print order(l,0)
    print order(l,3)
    print median(l)
    print mode(l)
    print variance(l)
    print stdev(l)

if __name__ == '__main__':
    main()
