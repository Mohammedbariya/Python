
from datetime import datetime
from os import remove
import os

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


abc = True    
while abc == True:
    try:
        with open("Bookslist.txt","r") as r:
            m = r.read()
            w =r.readlines()
    except FileNotFoundError :
        with open("Bookslist.txt","w") as r:
            r.write("")
    abc = False  

with open("Bookslist.txt","r") as r:
    w =r.readlines()          

s =[]
for item in w:
    s.append(item)
s = list(map(lambda s: s.strip(), s))

if ('') in s:
    
    while '' in s:
        s.remove('')

with open("Bookslist.txt","w") as hk:
    for item in s:
        hk.write(f"{item}\n")    


class library:
    def __init__(self,listofbooks):
        self.books = listofbooks

    def displayavailablebooks(self):
        with open("Bookslist.txt","r") as m:
           t = m.read()
            
        if t =="":
            print("No books are available in library right now")
        else:    
            index = 0
            for book in self.books:
                index +=1
                print(f"{index}.{book}\n",end=(""))

    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"library giving you {bookname}, Please keep it safe and returned it with in 30 days")
            with open("libraryinfo.txt","a") as f:
                f.write(f"The {bookname} book has been borrowed by {studentname} at {dt_string}\n") 
                with open(f"{studentname}.txt","a") as e:
                    e.write(f"{bookname}")
                    e.write("\n")     

            self.books.remove(bookname)
            with open("Bookslist.txt","w")as r:
                for item in self.books:
                    r.write(f"{item}\n")
            return True
        else:
            print("Sorry! The book you want is not available ")    
            return False
    def addbook(self,bookname):
        self.books.append(bookname)
        with open("libraryinfo.txt","a") as f:
            f.write(f"The {bookname} book has been added to library by {studentname} at {dt_string}\n")    
        with open("Bookslist.txt",'r') as q:
            wq = q.read()
        if wq == "":
            with open("Bookslist.txt",'a') as q:
                q.write(bookname)
            print("Book added to list")        
        else: 
            with open("Bookslist.txt","a") as df:
                df.write(f"\n{bookname}")     
            print("Book added to list")


    def returnbook(self,bookname):
        with open("libraryinfo.txt","a") as f:
            f.write(f"The {bookname} book has been returned by {studentname} at {dt_string}\n")
        with open(f"{studentname}.txt","r") as e:
            s = e.readlines()
        with open(f"{studentname}.txt","w") as e:
            
            p =[]
            for item in s:
                p.append(item) 
            p = list(map(lambda p: p.strip(), p))    
                   
            if bookname in p:
                p.remove(bookname)
                with open(f"{studentname}.txt","w") as y:
                    for item in p:
                        y.write(f"{item}\n")
                        
                
        self.books.append(bookname)                                
        print("Thank you for returning the book hope you enjoy the book ") 

class student:

    def requestbook(self):
        self.books = input("Enter the name of the book you want to borrow: ")
        return self.books

    def returnbook(self):
        with open(f"{studentname}.txt","r") as r:
            q = r.readlines()
            q = list(map(lambda q: q.strip(), q))
            print(f"Which book do you want return?")
            number= 0
            for i in q:
                number += 1
                print(f"{number}.{i}")
        y= True
        while y == True:
            
            self.books = input("Enter the name of the book you want to return : ")
            if self.books =="":
                print("Please enter a proper book name")
                y= True
            else:
                with open("Bookslist.txt","r")as r: 
                    re = r.read()
                if re == "":
                    with open("Bookslist.txt","a")as r:
                        r.write(self.books)
                else:          
                    with open("Bookslist.txt","a")as r:
                        r.write(f"\n{self.books}")
                return self.books


if __name__ == "__main__":
    centrallibrary = library(s)
    student = student()
    welcomemsg = " \n ===== Welcome to the central library====="
    print(welcomemsg)
    studentnam = input("Enter your name: ")
    studentname = studentnam.lower()


    while (True):
        option = '''\nPlease choose one option:

        1. List all available books
        2. Request a book
        3. Return a book
        4. Add a book to library
        5. Exit the Library
        
        '''

        print(option)
        a = True
        while a ==True:
            try:
                c = int(input("Enter your option(Enter a number):"))
                a = False
                if c == 1:
                    centrallibrary.displayavailablebooks()
                elif c == 2:
                    centrallibrary.borrowbook(student.requestbook())
            
                elif c == 3:
                    centrallibrary.returnbook(student.returnbook())
                elif c == 4:
                    bookname = input("Enter book name:")
                    centrallibrary.addbook(bookname)


                elif c == 5:
                    try:
                        with open(f"{studentname}.txt","r") as r:
                            e = r.read()
                        if e == "":
                            os.remove(f'{studentname}.txt')
                        print("Thanks for visiting central library")
                        exit()
                    except Exception:
                        print("Thanks for visiting central library")
                        exit()
                else:
                    print("Invalid choice")
            except Exception as e:
                print("Please enter a valid value")
                a = True 
                    