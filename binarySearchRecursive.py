def binary_search_recursive(my_list, target):
    if len(my_list) == 0:
        return False
    else:
        midpoint = len(my_list) // 2

    if my_list[midpoint] == target:
        return True
    else:
        if my_list[midpoint] < target:
            return binary_search_recursive(my_list[midpoint+1:], target)
        else:
            return binary_search_recursive(my_list[:midpoint], target)


def verify(result):
    print(f"Target found: {result}")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
verify(binary_search_recursive(numbers, 7))
verify(binary_search_recursive(numbers, 15))
