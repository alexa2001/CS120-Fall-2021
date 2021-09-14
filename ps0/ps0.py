#################
#               #
# Problem Set 0 #
#               #
#################



#
# Setup
#

class BinaryTree:
    # left : BinaryTree
    # right : BinaryTree
    # key : string
    # temp : int
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.temp = None



#
# Problem 1
#

# Sets the temp of each node in the tree T
# ... to the size of that subtree
def calculate_size(T):
    # Set the temp for each node in the tree
    # The return value is up to you
    
    # Your code goes here
    T.temp = 1
    if T.left:
        calculate_size(T.left)
        T.temp += calculate_size(T.left).temp

    if T.right:
        calculate_size(T.right)
        T.temp += calculate_size(T.right).temp
    return T 

#
# Problem 3
#

# Outputs a subtree subT of T of size in the interval [L,U] 
# ... and removes subT from T by replacing the pointer 
# ... to subT in its parent with `None`
def FindSubtree(T, L, U): 
    # Instructions:
    # Implement your Part 2 proof in O(n)-time
    # The return value is a subtree that meets the constraints

    # Your code goes here

    tree = calculate_size(T)
    return checkTree(tree, L, U)
    
    
def checkTree(T, L, U):
    if T.left: #if left subtree exists
        if T.left.temp >= L and T.left.temp <= U: #if size(left subtree) is in interval [L, U] return subtree
            subtree = T.left 
            T.left = None
            return subtree
        else:
            return FindSubtree(T.left, L, U) #keep searching in left subtree
    elif T.right: #if right subtree exists
        if T.right.temp >= L and T.right.temp <= U: #if size(right subtree) is in interval [L, U] return subtree
            subtree = T.right
            T.right = None
            return subtree
        else:
            return FindSubtree(T.right, L, U) #keep searching in right subtree

    return None


