def split_lists(list_1, list_2):
    result_list = []
    for i in list_1:
        if isinstance(i, int) and -10 < i <= 10:
            if i in list_2:
                result_list.append(i)
    result_list.sort(reverse=True)
    return result_list


list_1 = [1, 3, 4]
list_2 = [2, 3, 5]
# print(split_lists(list_1, list_2)
print(split_lists(list_1, list_2) == [3])
# негативный нет совпадении
list_1 = [1, 3, 4]
list_2 = [2, 6, 5]
print(split_lists(list_1, list_2) == [])
list_1 = [2, 3, 4]
list_2 = [-2, 6, "A"]
print(split_lists(list_1, list_2) == [])
