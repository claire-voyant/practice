import sys

# Linked list class

class Linked_List:
    '''
    List_Node is an inner class of the Linked_List class.
    It stores a value, and a pointer to the next List_Node.
    Note the __repr__ method, which shows the addresses in
    the next pointers, so you can compare several nodes and
    verify that they are indeed linked together correctly.
    '''
    class List_Node:
        def __init__(self, value = None, next = None):
            self._value = value
            self._next = next

        def __str__(self):
            return '(' + str(self._value) + ')'

        def __repr__(self):
            result = '('
            result += '(@' + str(id(self)) + ' ' + repr(self._value) + ') -> '
            if self._next == None:
                result += 'None)'
            else:
                result += str(id(self._next))
                result += ')'
            return result

    '''
    List constructor.  Can be invoked in three ways:
    Linked_List() returns an empty list.
    Linked_List(<another Linked_List>) makes a copy of the other list.
    Linked_List(<a python list>) returns a list containing the list's values.
    '''
    def __init__(self, orig = None):
        self._head = None
        self._size = 0
        if orig != None and \
           (type(orig) == list or type(orig) == Linked_List):
            for x in orig:
                self.add_tail(x)

    def copy(self, other):
        return Linked_List(other)

    '''
    Iterator, invoked in code like this:
       for x in list:
    '''
    def __iter__(self):
        previous_nodes = set()
        current = self._head
        while current != None:
            previous_nodes.add(current)
            yield current._value
            if current._next in previous_nodes:
                print 'ERROR: circular reference at node',repr(current)
                break
            current = current._next

    '''
    Membership test, invoked in code like this:
       if x in list:
    '''
    def __contains__(self, value):
        
        previous_nodes = set()
        current = self._head
        while current != None:
            previous_nodes.add(current)
            if current._value == value:
                return True
            elif current._next in previous_nodes:
                print 'ERROR: circular reference at node',repr(current)
                break
            current = current._next
        return False        

    '''
    Printable version of the list.
    '''
    def __str__(self):
        previous_nodes = set()
        result = '('
        current = self._head
        while current != None:
            previous_nodes.add(current)
            result += str(current._value)
            if current._next != None:
                result += ' '
            if current._next in previous_nodes:
                result += '[CIRCULAR link here]'
                break
            else:
                current = current._next
        result += ')'
        return result

    '''
    Programmer-friendly printable version of the list.
    '''
    def __repr__(self):
        result = 'Linked_List(\n'
        current = self._head
        previous_nodes = set()
        while current != None:
            previous_nodes.add(current)
            result += '  ' + repr(current)
            if current == self._head:
                result += ' == head'
            if current._next == None:
                result += ' == tail'
            if current._next in previous_nodes:
                result += ' ERROR: circular reference\n'
                break
            else:
                current = current._next
            result += '\n'
        result += ')'
        return result

    '''
    Add a node before the head node.
    You must modify this method.
    '''
    def add_front(self, value):
        self._head = self.List_Node(value, self._head)
        self._size += 1

    '''
    Add a node after the tail node.
    You must modify this method.
    '''
    def add_tail(self, value):
        new_node = self.List_Node(value)
        if self._head == None:
            self._head = new_node
            self._size += 1
        else:
            current = self._head
            while current._next != None:
                current = current._next
            current._next = new_node
            self._size += 1

            '''
            Uncommenting these two lines produces a circular list
            Try it, and print the list.
            '''
#            if value == 5:
#                current._next._next = self._head

    '''
    Retrieve entry in list at given index
    '''
    def __getitem__(self, index):
        if type(index) != int:
            raise TypeError
        elif 0 <= index and index < len(self):
            current = self._head
            for i in xrange(index):
                current = current._next
            return current._value
        else:
            raise IndexError

    '''
    Insert value into list, at given index.
    '''
    def insert(self, value, index):
        if type(index) != int:
            raise TypeError
        elif index > len(self):
            raise IndexError
        elif index == 0:
            self.add_front(value)
        elif index == len(self):
            self.add_tail(value)
        else:
            prev = self._head
            for i in xrange(index - 1):
                prev = prev._next
            new_node = self.List_Node(value, prev._next)
            prev._next = new_node
            self._size += 1

    '''
    Remove entry in list, at given index
    '''
    def __delitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError
        else:
            if index == 0:
                victim = self._head
                self._head = self._head._next
                self._size -= 1
            else:
                prev = self._head
                for x in xrange(index - 1):
                    prev = prev._next
                victim = prev._next
                prev._next = victim._next
                self._size -= 1
            return victim._value

    '''
    ------------------------------------------------------------------
    ALL THE CODE YOU MUST MODIFY IS BELOW THIS LINE
    vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    '''

    '''
    True or False if the list is/isn't empty.
    You must modify this method.
    '''
    def is_empty(self):
        self.update_size()
        return self._size <= 0
    
    '''
    Recompute the _size field.
    You must modify this method,
    and also these methods:
    __init__, add_head, add_tail, __insert__, __delitem__

    '''
    def update_size(self):
        real = 0
        for x in self:
          real += 1
        self._size = real 
    
    '''
    Return self._size
    You must modify this method.
    '''
    def __len__(self):
        return self._size

    '''
    Return the VALUE in the head node, or None if empty.
    You must modify this method.
    '''
    def first(self):
        if self.is_empty():
          return None
        
        return self[0]
 
    '''
    Return the VALUE in the tail node, or None if empty.
    You must modify this method.
    '''
    def last(self):
        if self.is_empty():
          return None
        return self[len(self)-1]

    '''
    Return a new Linked_List, with self's values stored in 
    reverse order.
    Create a result Linked_List, visit each value in self,
    and add it to the result's head.  Return the result.
    You must modify this method.
    '''
    def reversed(self):
        p = Linked_List()
        index = len(self) -1
        for x in self: 
          p.add_tail(self[index])
          index -= 1
        return p

    '''
    Add the value to the front of the list.
    You must modify this method.
    '''
    def push_front(self, value):
        self.add_front(value)
    
    '''
    Add the value to the end of the list.
    You must modify this method.
    '''
    def push_back(self, value):
        self.add_tail(value)
    
    '''
    Remove the value from the front of the list.
    RETURN that value. 
    Raise IndexError if list is empty.
    You must modify this method.
    '''
    def pop_front(self):
        if self.is_empty():
          raise IndexError
        front = self[0]
        del self[0]
        return front
    
    '''
    Remove the value from the end of the list.
    RETURN that value.
    Raise IndexError if list is empty.
    You must modify this method.
    '''
    def pop_back(self):
        if self.is_empty():
          raise IndexError
        back = self[len(self)-1]
        del self[len(self)-1]
        return back
    
    '''
    Remove the node at the given index, and return its old value.
    Raise TypeError if index is not an int.
    Raise IndexError if index is out of bounds.
    You must modify this method.
    '''
    def pop(self, index):
        if type(index) != int:
          raise TypeError
        if ((index < 0) or (index >= len(self))):
          raise IndexError
        r = self[index]
        del self[index]
        return r

    '''
    Return a new list, which is the set difference:
    self minus other.
    Create a result list, and append to it every value in this
    list, but only if the value is NOT in other.
    Raise TypeError if other_list is not a python list, a set,
    or a linked_list
    You must modify this method.
    '''
    def __sub__(self, other_list):
        t = type(other_list)
        r = Linked_List()
        for x in self:  
          cap = 1
          for y in other_list:
            if x != y and cap != 0:
              cap += 1
            if x == y:
              cap = 0
          if cap != 0:
            cap = 1
            r.push_back(x)
        return r

    '''
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ALL THE CODE YOU MUST MODIFY IS ABOVE THIS LINE
    ------------------------------------------------------------------
    '''

def main():
    pi = Linked_List([3, '.', 1, 4, 1, 5])

    pi.update_size()

    print 'Should be 6:     ', len(pi)
    print 'Should be False: ', pi.is_empty()
    print 'Should be True:  ', Linked_List().is_empty()

    print 'First and last:  ', pi.first(), pi.last()
    print 'PI reversed:     ', pi.reversed()
    pi.push_front('PI =')
    pi.push_back( '...')
    print 'After pushes:    ', pi
    print 'Size should be 8:', len(pi)
    front = pi.pop_front()
    back  = pi.pop_back()
    print 'Front and back:  ', front, back
    print 'After pops:      ', pi
    pi.pop(1)
    print 'No dot:          ', pi
    print 'Minus[1,2]:      ', (pi - Linked_List([1,2]))
if __name__ == '__main__': main()



