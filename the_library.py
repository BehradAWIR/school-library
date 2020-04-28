##IMPORTS
from sys import stderr

##CLASS DEFINED
class Student:
    def __init__(self, username):
        self.username = username

    def show(self):
        print(self.username)

    def show_all(self):
        print(self.username, end="")


class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = int(price)

    def show(self):
        print ("title: ",self.title, " | price: ", self.price)


##FUNCTIONS
def error(key):
    if key == None:
        return
    print("Error:", ERRORS[key], file=stderr)
    return


##INITIAL VARS
ERRORS = {'NotFoundUser': "the username was not found, please try again",
          'invalReq': "the request is invalid, please try again",
          'invalString':"sorry, please enter a number",
          'NotFoundBook': "the book was not found, please try again",
          'usedUser': "sorry, the username has been taken",
          'usedTitle': "sorry, but a book with the same title exists"}

new_std = Student("Mojtaba")
books = []
students = [new_std]

##MAIN
while True:
    cmd = input("please enter a command or ask for help using '-h': ")
    ##COMMADS RELATED TO STUDETNS
    if cmd == '-h':
        print ("welcome to the schools library! \n here you can use a bunch of commands for accessing, deleting or adding data to the base \n")
        print ("add using: \n 'add student' ==> for adding a student \n 'add book' ==> for adding a book \n")
        print ("access using: \n 'show students' ==> for accessing all students gathered data \n 'show student' ==> for accessing a special student's data \n 'show books' ==> for accessing all books gathered data \n 'show book' ==> for accessing a specific book's data \n")
        print ("remove data: \n 'del student' ==> to remove a specific piece of information related to a student \n 'del book' ==> to remove a specific piece of information related to a book \n")
    elif cmd == "add student":
        while_flag=True
        while (while_flag):
            username = input("please enter the chosen username or 'return': ")
            if username == "return":
                while_flag=False
                continue
            flag = True
            for i in students:
                if i.username == username:
                    error("usedUser")
                    flag=False

            if (flag):
                new_std = Student(username)
                students.append(new_std)
                while_flag = flag = False
    elif cmd == "show students":
        for i in students:
            if (i.username != "Mojtaba"):
                print(" ", end = "")
            i.show_all()
        print ("")
    elif cmd == "show student":
        flag = True
        while (flag):
            username = input("please enter a username or 'return': ")
            if username == "return":
                flag=False
                continue
            for i in students:
                if i.username == username:
                    i.show()
                    flag=False
                    break
            if flag:
                error('NotFoundUser')
    elif cmd == "del student":
        while_flag = True
        while while_flag:
            username = input("please enter a username or 'return: ")
            if username=="return":
                while_flag=False
                continue
            flag=True
            for i in range(len(students)):
                if (username == students[i].username):
                    ans = input ("are you sure of deleting this username?(yes/ no)")
                    flag=False
                    while_flag = False
                    if (ans == "yes"):
                        students.pop(i)
                        break
            if flag:
                error("NotFoundUser")

    ##COMMANDS RELATED TO BOOKS
    elif cmd == "add book":
        flag=True
        while (flag):
            bookName = input("please enter the chosen book's name or 'return': ")
            if (bookName == "return"):
                flag = False
                continue
            used_flag = False
            for i in books:
                if i.title == bookName:
                    error("usedTitle")
                    used_flag = True
                    break
            if (used_flag):
                continue
            try:
                bookPrice = int(input("please enter the book's price: "))
                new_book = Book(bookName, bookPrice)
                books.append(new_book)
                flag = False
            except ValueError:
                error("invalString")
                
    elif cmd == "show books":
        for i in range(len(books)):
            print(i+1,") ", end="")
            books[i].show()
            
    elif cmd == "show book":
        flag=True
        while (flag):
            bookTitle = input("please enter the chosen book's title or 'return': ")
            if (bookTitle == "return"):
                flag = False
                continue
            for i in books:
                if i.title == bookTitle:
                    i.show()
                    flag=False
            if flag:
                error("NotFoundBook")

    elif cmd == "del book":
        flag=True
        while (flag):
            bookTitle = input("please enter the chosen book's title or return: ")
            if (bookTitle == "return"):
                flag = False
                continue
            for i in range(len(books)):
                if books[i].title == bookTitle:
                    books[i].show()
                    ans = input ("are you sure of deleting this book?(yes/ no)")
                    flag = False
                    if ans=="yes":
                        books.pop(i)
                        break
            if flag:
                error("NotFoundBook")
    elif cmd == "quit":
        ans = input ("are you sure? (yes/no)")
        if ans == "yes":
            break

    else:
        error("invalReq")
        
