# import string
#
# class alpha_beit:
#
#     def __init__(self, letter: str):
#         self.lower = string.ascii_lowercase
#         self.letter = letter.lower()
#         self.end = 'z'
#
#     def __iter__(self):
#         self.counter = self.lower.index(self.letter)
#         return self
#
#     def __next__(self):
#         if self.counter > self.lower.index(self.end):
#             raise StopIteration()
#         curr = self.lower[self.counter]
#         self.counter += 1
#         return curr
#
#
# def get_next_letters(letter: str):
#     for i in alpha_beit(letter):
#         return i
#
#
# # if __name__ == '__abc_itter__':
# letter = input('insert letter')
# try:
#     print(get_next_letters(letter))
# except ValueError:
#     print('not_letter')

# def judgeCircle(moves: str) -> bool:
#     sum = 0
#     for let in moves:
#         if let == 'U' or let == 'R':
#             sum += 1
#         elif let == 'D' or let == 'L':
#             sum -= 1
#     if sum == 0:
#         return True
#     else:
#         return False
#
#
# print(judgeCircle('UD'))
