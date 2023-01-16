# Filter elements - by creating a new filtered list
# less efficient in terms of memory
# drinks = ['juice', 'wine', 'beer', 'coca-cola',
#           'sprite', 'martini', 'coffee', 'tea']
# filtered_drinks = []
# for drink in drinks:
#     if "i" not in drink:
#         filtered_drinks.append(drink)
# print(filtered_drinks)

# for i in range(len(drinks)):
#     if "i" not in drinks[i]:
#         filtered_drinks.append(drink[i])
# print(filtered_drinks)


# Remove elements inplace
# Bad code - not working!
drinks = ['juice', 'wine', 'beer', 'coca-cola',
          'sprite', 'martini', 'coffee', 'tea']
# for drink in drinks:
#     if "i" in drink:
#         drinks.remove(drink)
# print(drinks)
# for i in range(len(drinks)):
#     if "i" in drinks[i]:
#         drinks.pop(i)


# Correct code - option 1
# drinks = ['juice', 'wine', 'beer', 'coca-cola',
#           'sprite', 'martini', 'coffee', 'tea']
# indices_to_remove = []
# for i, drink in enumerate(drinks):
#     if "i" in drink:
#         indices_to_remove.append(i)
#
# indices_to_remove.sort(reverse=True)
# for i in indices_to_remove:
#     drinks.pop(i)
# print(drinks)

# Correct code - option 2
# drinks = ['juice', 'wine', 'beer', 'coca-cola', 'sprite', 'martini', 'coffee', 'tea']
# values_to_remove = []
# for drink in drinks:
#     if "i" in drink:
#         values_to_remove.append(drink)
#
# for val_to_remove in values_to_remove:
#     drinks.remove(val_to_remove)
# print(drinks)



# drinks = ['juice', 'wine', 'beer', 'coca-cola', 'sprite', 'martini', 'coffee', 'tea', 'wine']
# drinks_len = len(drinks)
# for i in range(drinks_len - 1, -1, -1):
#     drink = drinks[i]
#     if 'i' in drink:
#         drinks.pop(i)
# print(drinks)