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
    tree_list = []
    # construct tree node first
    for i in nums:
        if i is not None:
            i = TreeNode(i)
        tree_list.append(i)

    # build binary tree
    i = 0
    while 2 * i + 2 < len(nums):
        if tree_list[i] is not None:
            tree_list[i].left = tree_list[i * 2 + 1]
            tree_list[i].right = tree_list[i * 2 + 2]
        i += 1
    return tree_list[0]