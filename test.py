def sort(input_list, p, r):
    if len(input_list) <= 1:
        return input_list

    def partition(arr, p, r):
        pivot = arr[r]
        while i < j:
            while i < j and arr[i] <= pivot:
                i += 1
            arr[j] = arr[i]
            while i < j and arr[j] >= pivot:
                j -=1
            arr[i] = arr[j]

        arr[i] = pivot
        return i

    left



if __name__ == '__main__':
    normal_list = [4, 5, 6, -1, 3, 2, 1, 3]
    # normal_list = [1, 2, 3]
    print(sort(normal_list))
