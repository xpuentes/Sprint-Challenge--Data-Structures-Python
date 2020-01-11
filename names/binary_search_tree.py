import sys


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if new value is less than current node
        if value < self.value:
            # if there is no self.left value
            if not self.left:
                # set the new left child to be new value
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # the new value is greater than the current node
        # go right
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the root node, is the target value, we found the value
        if self.value == target:
            return True
            # target is smaller, go left
        sub_tree_contains = False
        if target < self.value:
            if not self.left:
                return False
            else:
                sub_tree_contains = self.left.contains(target)

        # target is greater, go right
        else:
            if not self.right:
                return False
            else:
                sub_tree_contains = self.right.contains(target)

        return sub_tree_contains

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None

        current_tree_root = self
        while current_tree_root.right:
            current_tree_root = current_tree_root.right

        return current_tree_root.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
