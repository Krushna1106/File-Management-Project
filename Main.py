
from pathlib import Path
import os
def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readfileandfolder()
        name = input("Enter The New File Name : ")
        p = Path(name)  # "p" shows the adress (path) of the new file "name" Stored.
        if not p.exists() or p.is_file():
            with open(p , 'w') as f:
                data = input("What You wnat To Write in File : ")
                f.write(data)
            print("FILE CREATED SUCESSFULLY. ")
        else:
            print("File Already Existed")
    except Exception as err:
        print(f"An Error Occured : {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Enter The File Name : ")
        p = Path(name)
        if p.exists() and p.is_file:
            with open(p , 'r') as f:
                data = f.read()
                print(data)
            print("File Readed Sucessfully")

        else:
            print("File Does Not Exist")
    except Exception as err:
        print(f"An Error Occured {err}")

def updatefile() :
    try:
        readfileandfolder()
        name = input("Enter The File Name To Update : ")
        p = Path(name)
        if p.exists() and p.is_file:
            print("Press 1 For Changing Name Of Your File \n"
                  "Press 2 For Overwriting the Data of Your File \n"
                  "Press 3 For Appending Some Content in Your File")
        
            res = int(input("Enter Your Response : "))

        if res == 1 :
            name2 = input("Enter the New Name Of File : ")
            p2 = Path(name2)
            p.rename(p2)
            print("File Renamed Sucessfully...")

        if res == 2 :
            with open(p , 'w') as f :
                res = input("Enter The Data To Overwrite : ")
                f.write(res)
                print("Data Overwritted Sucessfully")

        if res == 3 :
            with open(p , 'a') as f :
                res = input("Enter The Data To Append : ")
                f.write("" + res)
                print("Data Appended Sucessfully")
        else :
            print("File Does Not Exists ")
    except Exception as err:
        print(f"An error Occured as {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Enter The File Name To Delete : ")
        p = Path(name)
        if p.exists and p.is_file:
            os.remove(p)
            print("File Removed Sucessfully")
        else : 
            print("File Does Not Exists")
    except Exception as err:
        print(f"An error Occured as {err}")

        

print("Press 1 For Creating a File \n"
      "Press 2 For Reading a File \n"
      "Press 3 For Updating a File \n"
      "Press 4 For Deleting a File")

Check = int(input("Please Tell Your Response : "))

if Check == 1 :
    createfile()

if Check == 2 :
    readfile()

if Check == 3 :
    updatefile()

if Check == 4 :
    deletefile()


    


