'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()
        if xs:
            self.insert_list(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''

        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        ret = True
        if node is None:
            return True
        a = [1, 0, -1]
        if AVLTree._balance_factor(node) not in a:
            return False
        if node.left:
            if node.value >= BST._find_largest(node.left):
                ret &= AVLTree._is_avl_satisfied(node.left)
            else:
                ret = False
        if node.right:
            if node.value <= BST._find_largest(node.right):
                ret &= AVLTree._is_avl_satisfied(node.right)
            else:
                ret = False
        return ret

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node.right:
            new_root = Node(node.right.value)
            new_root.left = Node(node.value)
            new_root.right = node.right.right
            new_root.left.left = node.left
            new_root.left.right = node.right.left
            return new_root
        if node is None:
            return node

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node.left:
            new_root = Node(node.left.value)
            new_root.right = Node(node.value)
            new_root.left = node.left.left
            new_root.right.right = node.right
            new_root.right.left = node.left.right
            return new_root
        if node is None:
            return node

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if value is None:
            return
        if self.root is None:
            self.root = Node(value)
        else:
            return AVLTree._insert(value, self.root)

    @staticmethod
    def _insert(value, node):
        '''
        Added to help with insert function
        '''
        if node is None:
            return Node(value)
        if node.value > value:
            node.left = AVLTree._insert(value, node.left)
        if node.value < value:
            node.right = AVLTree._insert(value, node.right)
        return AVLTree._rebalance(node)

    def insert_list(self, xs):
        if self.root:
            for a in range(len(xs)):
                self.insert(xs[a])

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
            else:
                return AVLTree._left_rotate(node)
        if AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
            else:
                return AVLTree._right_rotate(node)
