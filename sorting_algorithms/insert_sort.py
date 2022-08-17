import time
from utils import make_random_list


class InsertSort:
    @staticmethod
    # common version
    def sort(input_list):
        if len(input_list) == 0:
            return []

        for i in range(len(input_list)):
            # swap if meet condition reversely
            for j in range(i)[::-1]:
                if input_list[i] < input_list[j]:
                    input_list[j], input_list[i] = input_list[i], input_list[j]
                    i -= 1
        return input_list

    @staticmethod
    # stop when no more change happen
    def sort2(input_list):
        if len(input_list) == 0:
            return []

        for i in range(len(input_list)):
            # swap if meet condition reversely
            for j in range(i)[::-1]:
                if input_list[i] < input_list[j]:
                    input_list[j], input_list[i] = input_list[i], input_list[j]
                    i -= 1
                else:
                    break
        return input_list

    @staticmethod
    # another version
    def sort3(input_list):
        if len(input_list) == 0:
            return []

        for i in range(len(input_list)):
            v = input_list[i]
            j = i - 1
            while j >= 0 and v < input_list[j]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                j -= 1
            input_list[j + 1] = v
        return input_list


if __name__ == '__main__':
    normal_list = [4, 5, 6, -1, 3, 2, 1, 3]
    empty_list = []
    insertSort = InsertSort()
    print("==========normal list==========")
    print(insertSort.sort3(normal_list))
    print("==========empty list==========")
    print(insertSort.sort3(empty_list))

    # time test
    print("==========time test==========")
    big_list = make_random_list(20000)
    start = time.time()
    insertSort.sort(big_list)
    print(f"insert_sort elapsed {time.time() - start}")
    start = time.time()
    insertSort.sort2(big_list)
    print(f"insert_sort2 elapsed {time.time() - start}")
    start = time.time()
    insertSort.sort3(big_list)
    print(f"insert_sort3 elapsed {time.time() - start}")
