class ListDivideException(Exception):
    
    def __init__(self, msg):
        self.msg = msg


def listDivide(numbers, divide=2):

    mylist = []
    for i in numbers:
        if i % divide == 0:
            mylist.append(i)
    return len(mylist)


def testListDivide():

    tests = [
        ([1, 2, 3, 4, 5]),
        ([2, 4, 6, 8, 10]),
        ([30, 54, 63, 98, 100]),
        ([]),
        ([1, 2, 3, 4, 5])
        ]
    for i in tests:
        if listDivide != divide:
            raise ListDivideException('Test Failed')
