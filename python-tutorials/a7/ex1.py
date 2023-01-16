goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]

longest_len = 0
longest_items = []
longest_indexes = []

for i, inner_goods in enumerate(goods):
    for j, item in enumerate(inner_goods):
        item_len = len(item)
        if item_len > longest_len:
            longest_len = item_len
            longest_items = [item]
            longest_indexes = [(i, j)]
        elif item_len == longest_len:
            longest_items.append(item)
            longest_indexes.append((i, j))

print(longest_len)
print(longest_items)
print(longest_indexes)

# get amount of vowels
# longest_vowels_cnts = []
# VOWELS = 'aeiou'
# for idx in longest_indexes:
#     longest_word = goods[idx[0]][idx[1]]
#     total_vowels_in_word = 0
#     for vowel in VOWELS:
#         total_vowels_in_word += longest_word.count(vowel)
#     longest_vowels_cnts.append(total_vowels_in_word)
#
# print(longest_vowels_cnts)
#
# # pretty print
# total_longest = len(longest_items)
# print(f"The length of the longest fruit1 name is: {longest_len}, "
#       f"and there are {total_longest} words with this length:")
# for i in range(total_longest):
#     # now each time we get to one of lists with index i, we
#     # receive the relevant element
#     print(f"The word {longest_items[i]} at index {longest_indexes[i]}, total vowels: {longest_vowels_cnts[i]}")