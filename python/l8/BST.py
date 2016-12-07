class BST:
    class Node:
        def __init__(self, x = None, l = None, r = None):
            self.data  = x
            self.left  = l
            self.right = r

        def is_leaf(self):
            return self.left == None and self.right == None

        def __str__(self):
            return '(' + str(self.data) + ')'

        def __repr__(self):
            result = '(' + repr(self.data) + ' @' + str(id(self)) +\
                      ' left -> '
            if self.left == None:
                result += 'None'
            else:
                result += '@' + str(id(self.left))
            result += ' right -> '
            if self.right == None:
                result += 'None'
            else:
                result += '@' + str(id(self.right))
            result += ')'
            return result
            
    def __init__(self, orig = None):
        self.root = None
        if orig != None:
            for x in orig:
                self.add(x)

#############################################################
#
# These methods will call the methods that YOU must implement
#
#############################################################

    def __len__(self):
        return self.subtree_size(self.root)

    def height(self):
        return self.subtree_height(self.root)

    def sum(self):
        return self.subtree_sum(self.root)

    def __contains__(self, value):
        return self.subtree_contains(value, self.root)

    def deepest_value(self):
        if self.root == None:
            return [None, 0]
        else:
            return self.subtree_deepest( self.root, 1)

######################################################################
#
# YOU MUST MODIFY THE METHODS BELOW THIS LINE
# (But look at the methods in the section just above,
#  to see how recursion starts)
#
# | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
# v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v

    ''' Exercise 1: return True if root is None '''
    def is_empty(self):
        if self.root == None:
          return True
        return False
   
    ''' Exercise 2: return 0 if node is None, 
        or 1 + sum or left and right sizes '''
    def subtree_size(self, node):
        if node == None:
          return 0
        else:
          return 1 + self.subtree_size(node.left) + self.subtree_size(node.right)
        
    ''' Exercise 3: return 0 if node is None,
        or 1 + max of left and right heights '''
    def subtree_height(self, node):
        if node == None:
          return 0
        else:
          return 1 + max(self.subtree_size(node.left), self.subtree_size(node.right))

    ''' Exercise 4: start at root, and loop node = node.right '''
    def rightmost_data(self):
        if self.root == None:
          return None
        else:
          node = self.root.right
          while node.right != None:
            node = node.right
        return node

    ''' Exercise 5: return 0 if node is None,
        or data + left and right sums '''
    def subtree_sum(self,node):
        if node == None:
          return 0
        else:
          return node.data + self.subtree_sum(node.left) + self.subtree_sum(node.right)

    ''' Exercise 6: False if node is None,
        otherwise go right or left until you find value '''
    def subtree_contains(self, value, node):
        return False

    ''' Exercise 7: return node's data and depth, if it's a leaf,
        otherwise find deepest in both subtrees, return deeper pair '''
    def subtree_deepest(self, node, depth):
        return [None, 0]

# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
#
# THE METHODS YOU MUST MODIFY ARE ABOVE THIS LINE
#
#########################################################################

    def add(self, value):
#        print 'add: value=',value
#        print 'before add, tree is:',
#        print repr(self)
        
        if self.root == None:
            self.root = self.Node(value, None, None)
        else:
            p = self.root
            while True:
                if p.data == value:
                    return False
                elif value < p.data:
                    if p.left == None:
                        p.left = self.Node(value)
                        return True
                    else:
                        p = p.left
                else: # value > p.data
                    if p.right == None:
                        p.right = self.Node(value)
                        return True
                    else:
                        p = p.right

    def inorder(self):
        result = []
        self.inorder_into_list(self.root, result)
        return result

    def inorder_into_list(self, node, result):
#        print 'entering inorder_list.'
#        print '  node=',repr(node)
#        print '  result=',result
        
        if node != None:
            self.inorder_into_list(node.left, result)
            result.append(node.data)
            self.inorder_into_list(node.right, result)

    def __str__(self):
        l = self.inorder()
        return str(l)

    def __repr__(self):
        result = 'BST(\n'
        result += self.subtree_repr(self.root, 0)
        result += ')'
        return result

    def subtree_repr(self, node, depth):
        if node != None:
            r_repr = self.subtree_repr(node.right, depth+1)
            l_repr = self.subtree_repr(node.left,  depth+1)
            return r_repr + \
                   '  ' + '  ' * depth + repr(node) + '\n' +\
                   l_repr
        else:
            return ''

def main():
    empty_tree = BST()

    print ("Is it empty?", empty_tree.is_empty())
    
    tree = BST([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7])
    print ("Is it empty?", tree.is_empty())
    
    print ("tree values:", tree)
    print ("repr(tree):\n",repr(tree))

    print ("size:",len(tree))
    print ("height:",tree.height())
    print ("rightmost:",tree.rightmost_data())
    print ("sum:",tree.sum())
    print ("contains 5?", (5 in tree))
    print ("contains 0?", (0 in tree))
    [value, depth] = tree.deepest_value()
    print ("deepest value:",value,"at depth",depth)

if __name__ == '__main__':
  main()
















