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


def debug_post_order_traversal(node):
    if node.left_node is not None:  # exists for binary operations
        debug_post_order_traversal(node.left_node)
    if node.right_node is not None:  # exists for both binary and unary operations
        debug_post_order_traversal(node.right_node)
    if node.char != '':
        print(node.char)
    else:
        print('BLANK NODE')
