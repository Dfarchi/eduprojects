def filter_vowels(elem):
    return elem not in "aeiou"
vowels_filter = filter(filter_vowels, "Hello World")
