drinks = ['juice', 'wine', 'beer', 'coca-cola',
          'sprite', 'martini', ['coffee', 'tea']]
# print(drinks)
# drinks.append('water')
# print(drinks)
#
# word = 'watEr'
# print(word)
# ret_val = word.lower()
# print(word)
# print(ret_val)
#
# drinks[2] = 'milk'
# print(drinks)
#
# # drinks[10] = "Sdfsdf"
#
# drinks.insert(3, "whiskey")
# print(drinks)
#
fruits = ['apple', 'orange']
#
# drinks.extend(fruits)
#
# print(drinks)
#
# drinks.append(fruits)
#
# print(drinks)


# new_word = "hello " + "world"
# print(5 + "hello")
# print(str(5) + "hello")
# print("hello" * 'world')
# print("hello"*10)

print(drinks)
print(fruits)
my_l = drinks + fruits
print(my_l)
print(drinks)
print(fruits)
print(drinks[0] is my_l[0])


drinks.extend(fruits)
print(drinks)

print(fruits * 2)

name = 'Ziv'
my_name = f"Hello {name}"

w1 = 'apple'
w2 = 'banana'
# 'applebanana"
w3 = w1 + w2
w3 = f"{w1}{w2}"
w3 = "".join([w1, w2])
print(w3)


