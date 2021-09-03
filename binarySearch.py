# Binary search data structure algorithm
def binary_search(my_list, target):
    first = 0
    last = len(my_list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if my_list[midpoint] == target:
            return midpoint
        elif my_list[midpoint] > target:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return None


def verify(result) -> str:
    if result is not None:
        return f"The position of the target is {str(result)}"
    else:
        return "The target was not found"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(verify(binary_search(numbers, 4)))
print(verify(binary_search(numbers, 12)))
