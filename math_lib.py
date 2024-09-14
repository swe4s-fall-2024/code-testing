def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def compute_list_mean(in_list: list) -> float:
    if len(in_list) == 0:
        return 0
    list_sum = 0
    for val in in_list:
        list_sum += val
    return list_sum / len(in_list)
