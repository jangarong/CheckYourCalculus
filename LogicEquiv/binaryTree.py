class Node:
    """
    ------------------------------------------------------------------
    binaryTree.Node: CDT for binary tree nodes.
    ------------------------------------------------------------------
    """

    def __init__(self, parent_node=None, left_node=None, right_node=None, char=''):
        self.parent_node = parent_node
        self.left_node = left_node
        self.right_node = right_node
        self.char = char
