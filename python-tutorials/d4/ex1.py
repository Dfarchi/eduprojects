import string

#
def letter2idx_mapper(letter):
    if letter not in string.ascii_letters:
        raise Exception("Cannot provide index to a non-letter")
    return string.ascii_lowercase.find(letter) + 1

def letters2idx(letters: list[str]) -> list[int]:
    return list(map(letter2idx_mapper, map(str.lower, letters)))
    # return list(map((' ' + string.ascii_lowercase).find, map(str.lower, letters)))


if __name__ == '__main__':
    # should raise an exception
    try:
        letters2idx(['1', 5, 'r'])
    except Exception:
        print('expected error')
    print(letters2idx(['A', 'b', 'a', 'Z', 'g', 'G']))