def search(sequence, target, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        if sequence[lower] == target:
            assert sequence[lower] == target
            return lower

    else:
        middle = (lower + upper) // 2
        if sequence[middle] == target:
            return middle
        elif sequence[middle] > target:
            return search(sequence, target, lower, middle)
        else:
            return search(sequence, target, middle + 1, upper)


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(search(test_list, 5))
print(search(test_list, 6))
print(search(test_list, 7))
print(search(test_list, 8))
print(search(test_list, 9))
print(search(test_list, 10))
print(search(test_list, 11))
