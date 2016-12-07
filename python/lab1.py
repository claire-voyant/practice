def print_sorted(a, b, c):
    """This function prints the three numbers passed in,
       in sorted order.
       It only uses if, elif, elif, print
    """
    if a < b:
      if b < c:
        return [a,b,c]
      elif a < c:
        return [a,c,b]
      else:
        return [c,a,b]
    elif a < c:
      
    # CHANGE OR REMOVE THE LINE BELOW
    print 'print_sorted is not implemented'

def max_product(alist):
    """This function returns the largest product possible
       using distinct numbers from alist
    """
    mymax = alist[0] * alist[0]
    for each in range(0,len(alist)-1):
      for other in range(0, len(alist) - 1):
        if alist[each] == alist[other]:
          continue
        elif (alist[each] *alist[other]) >  mymax:
          mymax = alist[each] * alist[other]

    # CHANGE OR REMOVE THE LINE BELOW
    return mymax

def delete_at(alist, i):
    """This function returns a new list, with the item at
       location i removed
    """

    # CHANGE OR REMOVE THE LINE BELOW
    return alist[:i] + alist[(i+1):]

def insert_at(alist, i, x):
    """This function returns a new list, with x inserted
       at location i
    """

    # CHANGE OR REMOVE THE LINE BELOW
    return alist[:i] + [x] + alist[(i+1):]


# DO NOT CHANGE ANYTHING BELOW THIS LINE
def main():
    print_sorted(1,2,3)
    print_sorted(1,3,2)
    print_sorted(2,1,3)
    print_sorted(2,3,1)
    print_sorted(3,1,2)
    print_sorted(3,2,1)
    
    print max_product([10, 20, 11, 30, -3, 21])
    print max_product([21, 10, 20, 20, 11, 30, -3])
    print delete_at([1,2,3], 0)
    print delete_at([1,2,3], 1)
    print delete_at([1,2,3], 2)
    print insert_at([1,2,3], 0, 0)
    print insert_at([1,3], 1, 2)
    print insert_at([1,2,3], 3, 4)

if __name__ == '__main__':
    main()
