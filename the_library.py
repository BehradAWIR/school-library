##TODO
## MAKE A DEF TO PRINT A DICT
## MAKE ALL CMDS ADAPTED TO DICTIONARY SUSTEM

##IMPORTS
import json
from sys import stderr

##CLASS DEFINED
# class Student:
#     def __init__(self, username):
#         self.username = username

#     def show(self):
#         print(self.username)

#     def show_all(self):
#         print(self.username, end="")


# class Book:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = int(price)

#     def show(self):
#         print ("title: ",self.title, " | price: ", self.price)


##FUNCTIONS
def error(key):
    if key == None:
        return
    print("Error:", ERRORS[key], file=stderr)
    return

def full_list_dict_print(inp_list, dict_args):
    for i in inp_list:
        for j in dict_args:
            print (i[j], end=" ")
        print()

def dict_print(dicti):
    for key, val in dicti.items():
        print("    ",key,": ", val)
    print()

##INITIAL VARS
books = []
students = [] 

with open("books.json", "r") as j:
    books = json.load(j)

with  open("users.json", "r") as j:
    students = json.load(j)

with open("ERRORS.json", "r") as j:
    ERRORS = json.load(j)

##MAIN
while True:
    cmd = input("please enter a command or ask for help using 'h': ")
    ##HELP COMMANDS
    if cmd == 'h':
        helpFile = open('help.txt', "r")
        pr = helpFile.read()
        print (pr)

    ##COMMADS RELATED TO STUDENTS
    elif cmd == "add student":
        new_students_data = {"name": "",
                             "lastName" : "",
                             "e-mail": "",
                             "username": "",}
        new_students_data["name"] = input("please enter your name or 'return': ")
        if new_students_data["name"] == "return":
            continue

        new_students_data["lastName"] = input("please enter your lastname or 'return': ")
        if new_students_data["lastName"] == "return":
            continue

        while_flag=True
        while (while_flag):
            new_students_data["e-mail"] = input("please enter your e-mail adress or 'return': ")
            if new_students_data["e-mail"] == "return":
                while_flag=False
                continue
            execute_flag = True
            for i in students:
                if i["e-mail"] == new_students_data["e-mail"]:
                    print(i)
                    execute_flag = False
                    error("usedEmail")
                    new_students_data.pop("e-mail")
            if (execute_flag):
                break
        if not while_flag:
            continue

        while_flag=True
        while (while_flag):
            new_students_data["username"] = input("please enter a username or 'return': ")
            if new_students_data["username"] == "return":
                while_flag=False
                continue
            execute_flag=True
            for i in students:
                if i["username"] == new_students_data["username"]:
                    execute_flag == False
                    error("usedUser")

            if (execute_flag):
                break
            
        if not while_flag:
            continue
        
        students.append(new_students_data)
        print(students)
        with open("users.json", "w") as j:
            json.dump(students, j)
        print("task finished sucessfully")


    elif cmd == "show students":
        full_list_dict_print(students)
        print()

    elif cmd == "show student":
        flag = True
        while (flag):
            username = input("please enter a username or 'return': ")
            if username == "return":
                flag=False
                continue
            for i in students:
                if i["username"] == username:
                    print("user found successfully:")
                    dict_print(i)
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
                if (username == students[i]["username"]):
                    ans = input ("are you sure of deleting this students data?(yes/ no)")
                    flag=False
                    while_flag = False
                    if (ans == "yes"):
                        students.pop(i)
                        with open("users.json", "w") as j:
                            json.dump(students, j)
                        print("task achieved successfully")
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
        
