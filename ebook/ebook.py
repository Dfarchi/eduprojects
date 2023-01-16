# with open('my_text.txt', 'w') as fh:
#     fh.write("The sun is shining!\n")

# with open('my_text.txt', 'w') as fh:
#     fh.write("Hello!\n")

# with open('my_text.txt', 'a') as fh:
#     fh.write("SUN!\n")

# with open('data/new_text.txt', 'a') as fh:
#     fh.write("SUN!\n")


class Ebook:

    def __init__(self, path, words:int):
        with open(path) as fh:
            content = fh.read()
            self.page = ''
            self.pages = []
            pcounter = 0
            for word in content.split():
                self.page += ' '+word
                if pcounter % words == 0:
                    self.pages.append(self.page)
                pcounter = +1


        # self.chapters =[]

    def bookmark(self, page):
        return self.pages[page+1]




alice = Ebook('C\Users\user\Desktop\\alice in wonderlands', 50)

print(alice.pages[0])