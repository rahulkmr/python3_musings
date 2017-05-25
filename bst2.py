from itertools import islice


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(node):
    fringe = []
    while fringe or node:
        if node is not None:
            fringe.append(node)
            node = node.left
        else:
            node = fringe.pop()
            yield node.val
            node = node.right


def preorder(node):
    fringe = []
    while fringe or node:
        if node is not None:
            yield node.val
            if node.right is not None:
                fringe.append(node.right)
            node = node.left
        else:
            node = fringe.pop()



tree = Node(10,
            Node(7,
                 Node(3,
                      Node(1)),
                 Node(8,
                      None,
                      Node(9))),
            Node(13,
                 Node(11),
                 Node(14)))

print(list(inorder(tree)))
print(list(preorder(tree)))
