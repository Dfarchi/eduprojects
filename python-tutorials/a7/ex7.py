goods = [['apple', 'pear', 'peach', 'chery' ],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry']]


for fruits_list in goods:
    # print(fruits_list)
    for i in range(0, len(fruits_list), 2):
        fruits_list[i] = fruits_list[i] + '2'

print(goods)
