goods = [['apple', 'pear', 'peach', 'chery' ],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry'],
         ['dragonfruit', 'ananas', 'passionfruit']]

VOWELS = 'aeoiu'

words_indices = []

for words_list_idx in range(len(goods)):
    # iterate list of words
    for word_idx in range(len(goods[words_list_idx])):
        # iterate words
        for vowel in VOWELS:
            if goods[words_list_idx][word_idx].startswith(vowel):
                words_indices.append([words_list_idx, word_idx])

print(words_indices)
