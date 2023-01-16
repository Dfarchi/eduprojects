# import os.path
# import pickle
#
# class Line:
#     def __init__(self, line_num, origin, destination):
#         self._line_num = line_num
#         self._origin = origin
#         self._destination = destination
#         self._secret_paassword = "adftjhgdf"
#
#     @property
#     def origin(self):
#         return
#
#     @origin.setter
#     def origin(self, value):
#         pass
#
#
#     def get_line(self):
#         return self._line_num
#
# l = Line(345, "t", "y")
# l.origin = 'hyhh'
#
# class Company:
#
#     def __init__(self):
#         self._dict_by_number = {}
#         self._dict_by_origin = {}
#
#     def _validate_line_exists(self):
#         pass
#
#     def _update_line_in_dictionaries(self):
#         pass
#         #updating internal variables
#
#     def add_line(self, line_num:int, origin:str, dest:str):
#         self._validate_line_exists()
#         self._update_line_in_dictionaries()
#
#
#
# if __name__ == '__main__':
#
#     try:
#         if not os.path.exists("/my/path/to/file"):
#             company = Company()
#         else:
#             with open("/my/path/to/file", "rb") as f:
#                 company = pickle.load(f)
#             pass
#         # a lot of code
#         company.
#
#     except:
#         pass
#
#     finally:
#         with open("/my/path/to/file", "wb") as f:
#             pickle.dump(company, f)