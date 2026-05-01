def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))  # recursive call
        else:
            result.append(item)
    return result

# Input
input_list = [1, [2, 3], [4, [5, 6]], 7]

# Output
print(flatten_list(input_list))