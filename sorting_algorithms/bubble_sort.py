import time
from utils import make_random_list


class BubbleSort:
    @staticmethod
    # common version
    def sort(input_list):
        if len(input_list) == 0:
            return []
        for i in range(len(input_list) - 1):
            for j in range(len(input_list) - i - 1):
                if input_list[j] > input_list[j + 1]:
                    input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
        return input_list

    @staticmethod
    # loop all elements
    def sort2(input_list):
        if len(input_list) == 0:
            return []
        for i in range(len(input_list) - 1):
            for j in range(len(input_list) - 1):
                if input_list[j] > input_list[j + 1]:
                    input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
        return input_list

    @staticmethod
    # stop when no more change happen
    def sort3(input_list):
        if len(input_list) == 0:
            return []
        for i in range(len(input_list) - 1):
            flag = False
            for j in range(len(input_list) - i - 1):
                if input_list[j] > input_list[j + 1]:
                    flag = True
                    input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
            if flag is False:
                return input_list


if __name__ == '__main__':
    normal_list = [4, 5, 6, -1, 3, 2, 1, 3]
    empty_list = []
    bubbleSort = BubbleSort()
    print("==========normal list==========")
    print(bubbleSort.sort3(normal_list))
    print("==========empty list==========")
    print(bubbleSort.sort3(empty_list))

    # time test
    print("==========time test==========")
    big_list = make_random_list(10000)
    big_list.sort(reverse=True)
    start = time.time()
    bubbleSort.sort(big_list)
    print(f"bubble_sort elapsed {time.time() - start}")
    start = time.time()
    bubbleSort.sort2(big_list)
    print(f"bubble_sort2 elapsed {time.time() - start}")
    start = time.time()
    bubbleSort.sort3(big_list)
    print(f"bubble_sort3 elapsed {(time.time() - start)}")
