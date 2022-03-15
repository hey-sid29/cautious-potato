#Health management system
from unicodedata import name


def getdate():
    import datetime
    return datetime.datetime.now()
def logdata():
    print("enter client name: ")   #Client name are: Harry/Rohan/Vishal
    name= str(input())
    if name=="Harry":
        i=1
        while i==1:
            print("Which activity do you want to log in:\n 1 for Exercise\n 2 for food and diet")
            ch=int(input())
            if ch==1:
                f=open("Harry_Exercise.txt","a")
                print("Which exercise has harry performed recently: ")
                data=str(input())
                f.write(str([str(getdate())])+data+"\n")
                f.close()
                
            if ch==2:
                f1=open("Harry_Diet.txt","a")
                print("what has Harry eaten recently")
                data1=str(input())
                f1.write(str([str(getdate())])+data1+"\n")
                f1.close()
                
            print("Do you want to continue:\n 1 for Yes\n 0 for No")
            i=int(input())
    elif  name=="Rohan":
        i=1
        while i==1:
            print("Which activity do you want to log in:\n 1 for Exercise\n 2 for Food")
            ch=int(input())
            if ch==1:
                f=open("Rohan_Exercise.txt")
                print("which exercise has Rohan performed recently")
                data=str(input())
                f.write(str([str(getdate())])+data+"\n")
                f.close()
                
            if ch==2:
                f1=open("Rohan_Diet.txt","a")
                print("What did Rohan have recently")
                data1=str(input())
                f1.write(str([str(getdate())])+data1+"\n")
                f1.close()
                
            print("Do you want to continue:\n 1 for Yes\n 0 for No")
            i=int(input())
    elif name=="Vishal":
        i=1
        while i==1:
            print("Which activity do you want to log in:\n 1 for Exercise\n 2 for Diet ")
            ch==int(input())
            if ch==1:
                f=open("Vishal_Exercise.txt",'a')
                print("Which exercise has Vishal performed recently")
                data=str(input())
                f.write(str([str(getdate())])+data+"\n")
                f.close()
                
            if ch==2:
                f1=open("Vishal_Diet.txt",'a')
                print("What food did Vishal have")
                data1=str(input())
                f1.write(str([str(getdate())])+data1+"\n")
                f1.close()
                
            print("Do you want to continue:\n 1 for Yes\n 0 for No")
            i=int(input())
    else:
        print("Invalid entry")
def retrieveData():
    print("Enter Client name")
    name=str(input())
    if name=="Harry":
        print("what would you like to see:\n 1 for Exercise logs\n 2 for Diet logs for harry")
        ch=int(input())
        if ch==1:
            f=open("Harry_Exercise.txt")
            f.readlines()
            f.close()
        if ch==2:
            f1=open("Harry_Diet.txt")
            f1.readlines()
            f1.close()
    elif name=="Rohan":
        print("What would you like to see:\n 1 for Exercise Logs\n 2 for Diet logs")
        ch=int(input())
        if ch==1:
            f=open("Rohan_Exercise.txt")
            f.readlines()
            f.close()
        if ch==2:
            f1=open("Rohan_Diet.txt")
            f1.readlines()
            f1.close()
    elif name=="Vishal":
        print("What would you like to see:\n 1 for Exercise logs\n 2 for Diet logs")
        ch=int(input())
        if ch==1:
            f=open("Vishal_Exercise.txt")
            f.readlines()
            f.close()
        if ch==2:
            f1=open("Vishal_Diet.txt")
            f1.readlines()
            f1.close()
    else:
        print("Invalid input->record does not exist")
print("Welcome to Health Care Management System")
print("What would u like to see today:\n 1 to log data of patients\n 2 to display logs")
choice=int(input())
if choice==1:
    logdata()
elif choice==2:
    retrieveData()
else:
    print("invalid entry->no record")
    
        



        






