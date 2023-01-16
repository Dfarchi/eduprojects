# initializing
# implement __str__ using calls to base class methods
# list of all the persons - can get their age
# list of
import datetime

from lesson10.person import Student, Person, Lecturer, LeadLecturer

s1 = Student('Ziv', 'Attias', 'Yaffo', 'ziv@gmail.com',
             datetime.date(year=1998, month=8, day=23),
             2023)

s2 = Student('Noa', 'Belfer', 'Tel Aviv', 'noa@gmail.com',
             datetime.date(year=1998, month=8, day=23),
             2022)

p1 = Person('Daniel', 'Raz', 'Hod Hasharon', 'daniel@gmail.com',
            datetime.date(year=1996, month=9, day=17))

l1 = Lecturer('Valeria', 'Aynbinder', 'Netanya', 'daniel@gmail.com',
              datetime.date(year=1996, month=9, day=17),
              10)

ll = LeadLecturer('Israel', 'Israeli', 'Netanya', 'daniel@gmail.com',
                  datetime.date(year=1996, month=9, day=17),
                  10, 5)

l = [s1, s2, p1, l1, ll]



for p in l:
    print(p)
    # print(p.get_age())
    # print(p.grades)
    # print(type(p))
    # print(isinstance(p, Student))
    # print(isinstance(p, Person))

# print(s1)

# print(help(Student))

# d = {1:'a', 2:'b'}
# print(type(d.values()))










