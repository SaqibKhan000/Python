list26 = [[1, 2], [3, 4], [5, 6]]
def flatten_list(list):
    return [item for item in list for item in item]
print(flatten_list(list26))