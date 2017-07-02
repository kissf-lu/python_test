# -*- coding: utf8 -*-

# A binary tree class.
class Tree:

    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

    def __repr__(self, level=0, indent="    "):
        s = level*indent + self.label
        if self.left:
            s = s + "\n" + self.left.__repr__(level+1, indent)
        if self.right:
            s = s + "\n" + self.right.__repr__(level+1, indent)
        return s

    def __iter__(self):
         return inorder(self)
        
# Create a Tree from a list.
def tree(listt):
    n = len(listt)
    if n == 0:
        return []
    i = int(n / 2)
    return Tree(listt[i], tree(listt[:i]), tree(listt[i+1:]))
# A recursive generator that generates Tree labels in in-order.
def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x
        yield t.label
        for x in inorder(t.right):
            yield x

if __name__ == "__main__":
    # Show it off: create a tree.
    t = tree("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # Print the nodes of the tree in in-order.
    for x in t:
        print (x)
