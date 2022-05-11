"""TO DESIGN A LIBRARY MANAGEMENT SYSTEM"""



class Library_Management:

    def __init__(self, listofbooks, lib_name):
        self.listofbooks=listofbooks
        self.lib_name=lib_name
        self.dictbooks={}
    def issue_books(self, bookname, user):
        
        if bookname in self.listofbooks:
            if user in self.dictbooks.values() and bookname in self.dictbooks.keys():
                print("The book has already been issued")
            else:
                self.dictbooks.update({bookname:user})
        else:
            print("Entered book name doesnt exist")
        print(self.dictbooks)
    def add_books(self, donate_books):
        self.listofbooks.append(donate_books)
        print(self.listofbooks)
    def return_books(self,bookname):
        if bookname in self.dictbooks.keys():
            self.dictbooks.pop(bookname)
            print(self.dictbooks)
        else:
            print("Book has not been issued yet")
    def display_all_books(self, listofbooks):
         print(self.listofbooks)
if __name__=='__main__':
    libraryname="Heritage Library"
    listofbooks=["No Longer Human by Dazai Osamu", "Rashoumon by Akutagawa", "Flawless by Oda Sakunoske", "Ikigai", "MobyDick by Herman Melville"]
    lm=Library_Management(listofbooks, libraryname)
    print(f"Welcome to {libraryname}")
    print("""What do you want to do:\n
            1-Get a book issued\n
            2-Donate a book\n
            3-Return a book\n
            4-Display all books in library""")
    ch=int(input("Enter choice here: "))
    while True:
        if ch==1:
            print("which do you want to issue: ")
            bookname=input("Type here: ")
            print("What is your name")
            user=input("type here: ")
            lm.issue_books(bookname, user)
        elif ch==2:
            print("which book are you donating: ")
            book=input("Type here: ")
            lm.add_books(book)
        elif ch==3:
            print("Which book are you returning: ")
            book=input("type here:")
            lm.return_books(book)
        elif ch==4:
            lm.display_all_books(listofbooks)
        print ("Do you want to continue: Press Y for yes and N for no")
        r=input("Type here: ")
        if r=='Y':
            continue
        elif r=='N':
            break
        else:
            print("Wrong input:XXXX")


