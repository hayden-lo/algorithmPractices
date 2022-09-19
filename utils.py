import random


class LinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_random_list(nums):
    random_list = []
    for i in range(nums):
        rd = random.randint(0, nums)
        random_list.append(rd)
    return random_list


def build_binary_tree(nums):
    if len(nums) == 0:
        return None

    tree_list = []
    is_fill_left = True
    root = None
    for num in nums:
        tree_node = TreeNode(num) if num is not None else None
        if len(tree_list) == 0:
            root = tree_node
            tree_list.append(tree_node)
        elif is_fill_left:
            tree_list[0].left = tree_node
            is_fill_left = False
            if tree_node is not None:
                tree_list.append(tree_node)
        else:
            tree_list[0].right = tree_node
            is_fill_left = True
            if tree_node is not None:
                tree_list.append(tree_node)
            tree_list.pop(0)
    return root
