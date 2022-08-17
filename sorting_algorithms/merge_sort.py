import time
from utils import make_random_list


class MergeSort:
    @staticmethod
    # common version
    def sort(input_list):
        # deal with special case and crucial for not going into maximum depth
        if len(input_list) <= 1:
            return input_list

        mid = len(input_list) // 2

        # divide first
        left = MergeSort.sort(input_list[:mid])
        right = MergeSort.sort(input_list[mid:])

        # merge
        i = j = 0
        new_list = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                new_list.append(left[i])
                i += 1
            else:
                new_list.append(right[j])
                j += 1
        new_list += left[i:]
        new_list += right[j:]
        return new_list


if __name__ == '__main__':
    normal_list = [4, 5, 6, -1, 3, 2, 1, 3]
    empty_list = []
    MergeSort = MergeSort()
    print("==========normal list==========")
    print(MergeSort.sort(normal_list))
    print("==========empty list==========")
    print(MergeSort.sort(empty_list))

    # time test
    print("==========time test==========")
    big_list = make_random_list(20000)
    start = time.time()
    MergeSort.sort(big_list)
    print(f"merge_sort elapsed {time.time() - start}")
