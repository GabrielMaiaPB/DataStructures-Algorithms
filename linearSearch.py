# Linear search data structure algorithm
def linear_search(my_list, target):
    for i in range(0, len(my_list)):
        if my_list[i] == target:
            return i
    return None


def verify(result) -> str:
    if result is not None:
        return f"The position of the target is: {str(result)}"
    else:
        return "Target not found"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(verify(linear_search(numbers, 6)))
print(verify(linear_search(numbers, 12)))
