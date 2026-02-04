class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(self.title, self.author)

    def rename(self, title):
        self.title = title

    def about(self):
        print(self.title, self.author)


book1 = Book("Python Asoslari", "Nodirxon")
book2 = Book("Clean Code", "Robert Martin")

book1.describe()
book2.describe()

book1.rename("Advanced Python")
book1.about()
