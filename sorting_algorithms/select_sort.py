import time
from utils import make_random_list


class SelectSort:
    @staticmethod
    # common version
    def sort(input_list):
        if len(input_list) == 0:
            return []
        for i in range(len(input_list) - 1):
            for j in range(i, len(input_list)):
                if input_list[i] > input_list[j]:
                    input_list[i], input_list[j] = input_list[j], input_list[i]
        return input_list


if __name__ == '__main__':
    normal_list = [4, 5, 6, -1, 3, 2, 1, 3]
    empty_list = []
    selectSort = SelectSort()
    print("==========normal list==========")
    print(selectSort.sort(normal_list))
    print("==========empty list==========")
    print(selectSort.sort(empty_list))

    # time test
    print("==========time test==========")
    big_list = make_random_list(20000)
    start = time.time()
    selectSort.sort(big_list)
    print(f"select_sort elapsed {time.time() - start}")
