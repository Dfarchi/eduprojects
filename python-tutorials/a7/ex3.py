goods = [['apple', 'pear', 'peach', 'chery' ],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry'],
         ['dragonfruit', 'ananas', 'passionfruit']]

fruits_b = []
for words_list in goods:
    for fruit in words_list:
        if 'b' in fruit:
            fruits_b.append(fruit)

print(fruits_b)