import time
from utils import make_random_list


class QuickSort:
    @staticmethod
    # common version
    def sort(input_list):
        # deal with special case and crucial for not going into maximum depth
        if len(input_list) <= 1:
            return input_list

        # partition
        left, right = [], []
        pivot = input_list[-1]

        for i in input_list[:-1]:
            if pivot < i:
                right.append(i)
            else:
                left.append(i)

        return QuickSort.sort(left) + [pivot] + QuickSort.sort(right)

    @staticmethod
    # swap method to save extra space
    def sort2(input_list, i, j):
        # deal with special case and crucial for not going into maximum depth
        if len(input_list) <= 1:
            return input_list

        def partition(arr, i, j):
            pivot = arr[i]
            while i < j:
                while i < j and arr[i] <= pivot:
                    i += 1
                arr[j] = arr[i]
                while i < j and arr[j] >= pivot:
                    j -= 1
                arr[i] = arr[j]

            arr[i] = pivot
            return i

        if i < j:
            mid = partition(input_list, i, j)
            QuickSort.sort2(input_list, i, mid - 1)
            QuickSort.sort2(input_list, mid + 1, j)


if __name__ == '__main__':
    normal_list = [4, 5, 6, -1, 3, 2, 1, 3]
    empty_list = []
    QuickSort = QuickSort()
    # print("==========normal list==========")
    # print(QuickSort.sort(normal_list))
    # print("==========empty list==========")
    # print(QuickSort.sort(empty_list))

    print("==========normal list==========")
    print(normal_list)
    print(QuickSort.sort2(normal_list, 0, len(normal_list) - 1))
    print(normal_list)
    print("==========empty list==========")
    print(empty_list)
    print(QuickSort.sort2(empty_list, 0, len(empty_list) - 1))
    print(empty_list)

    # time test
    print("==========time test==========")
    big_list = make_random_list(20000)
    start = time.time()
    QuickSort.sort(big_list)
    print(f"quick_sort elapsed {time.time() - start}")
