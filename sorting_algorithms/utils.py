import random


def make_random_list(nums):
    random_list = []
    for i in range(nums):
        rd = random.randint(0, nums)
        random_list.append(rd)
    return random_list
