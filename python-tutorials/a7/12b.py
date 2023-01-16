goods = [['apple', 'pear', 'peach', 'chery' ],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry']]

new_list = []

for fruits_list in goods:
    for fruit in fruits_list:
        new_word = fruit[-3:][::-1] + fruit[:-3]
        new_list.append(new_word)

print(new_list)