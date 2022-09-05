def sort(input_list):
    def dfs(idx, path):
        if idx == len(input_list):
            result.append(path[:])
            return

        for i in range(len(input_list)):
            if check_list[i] == 0:
                path.append(input_list[i])
                check_list[i] = 1
                dfs(idx + 1, path)
                path.pop()
                check_list[i] = 0

    check_list = [0 for i in range(len(input_list))]
    result = []
    dfs(0, [])
    return result


if __name__ == '__main__':
    # normal_list = [4, 5, 6, -1, 3, 2, 1, 3]
    normal_list = [1, 2, 3]
    print(sort(normal_list))
