import time
from utils import make_random_list


class InsertSort:
    @staticmethod
    # common version
    def sort(self, input_list):
        if len(input_list) == 0:
            return []
        for i in range(len(input_list)):
            # swap if meet condition reversely
            for j in range(i)[::-1]:
                if input_list[i] < input_list[j]:
                    input_list[j], input_list[i] = input_list[i], input_list[j]
                i -= 1
        return input_list


if __name__ == '__main__':
    normal_list = [4, 5, 6, -1, 3, 2, 1, 3]
    empty_list = []
    insertSort = InsertSort()
    print("==========normal list==========")
    print(insertSort.sort(normal_list))
    print("==========empty list==========")
    print(insertSort.sort(empty_list))

    # time test
    print("==========time test==========")
    big_list = make_random_list(10000)
    start = time.time()
    insertSort.sort(big_list)
    print(f"select_sort elapsed {time.time() - start}")
