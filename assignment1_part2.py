class Book(object):
    

    author = ''
    title = ''

    def __init__(self, author, title):
        
        self.author = author
        self.title = title

    def display(self):
        
        print "{}, written by {}".format(self.title, self.author)

B1 = Book('John Steinbeck', 'Of Mice and Men')
B2 = Book('Harper Lee', 'To Kill A Mockingbird')

B1.display()
B2.display()