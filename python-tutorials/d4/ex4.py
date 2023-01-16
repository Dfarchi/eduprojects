fruits =  ["apple", "ananas", "banana", "pear"]
print(list(filter(lambda fruit: fruit.count("a") >= 2, fruits)))