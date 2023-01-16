goods = [['apple', 'pear', 'peach', 'chery' ],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry']]

new_list = []

for fruits_list in goods:
    for fruit in fruits_list:
        new_list.append(fruit[:-3])

print(new_list)