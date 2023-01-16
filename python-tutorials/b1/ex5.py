def unique_tuple(original_tuple: tuple) -> tuple:
    # Option I
    # unique_list = []
    # for elem in original_tuple:
    #     if elem not in unique_list:
    #         unique_list.append(elem)
    # return tuple(unique_list)

    # Option II
    unique_set = set(original_tuple)
    return tuple(unique_set)


result = unique_tuple(("apple", 5, "banana", 5, "apple")) # -> ("apple", 5, "banana")
# ["apple", 5, "banana"]
print(result)

# user_input = input("Insert your values separated by comma: ")
#
# # convert string to tuple
# split_list = user_input.split(",")
# split_tuple = tuple(split_list)
# result = unique_tuple(split_tuple)
# print(result)