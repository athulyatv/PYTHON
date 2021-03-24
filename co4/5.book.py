class Publisher:
    def __init__(self, publisher):
        self.publisher = publisher

    def display(self):
        print("Publisher name:", self.publisher)


class Book(Publisher):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Title of the book :", self.title)
        print("Author of the book:", self.author)


class Python(Book):
    def __init__(self, pub, author, title, price, no):
        self.price = price
        self.no_of_pages = no
        Book.__init__(self, title, author)
        Publisher.__init__(self, pub)

    def display(self):
        super().display()
        print("Price of the book:", self.price)
        print("Number of pages in the book", self.no_of_pages)


b1 = Python("American Institute of Physics", "Kenneth W. Ford", "The Quantum World – Quantum Physics for Everyone", 1200, 300)
b1.display()
