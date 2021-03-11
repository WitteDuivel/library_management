import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="2zkNKcz&EOZaRjc$",database="library")
mycursor=mydb.cursor()
BorrowersID=int(input("ENTER YOUR BORROWER_ID:- "))
mycursor.execute("INSERT INTO BOOKS [borrowers_ID] VALUES(BorrowersID)")
bookID=input("ENTER THE BOOK'S ID:- ")
mycursor.execute("INSERT INTO BOOKS [book_ID] VALUES(bookID)")
bk_title=input("ENTER THE BOOK'S TITLE:- ")
mycursor.execute("INSERT INTO BOOKS [bktitle] VALUES(bk_title)")
stafforstudent=input("ARE YOU A STAFF MEMBER OR A STUDENT? (STAFF/STUDENT)")
if stafforstudent.upper()=="STAFF":
    staffID=int(input("ENTER YOUR STAFF_ID:- "))
    mycursor.execute("INSERT INTO BOOKS [staff_ID] VALUES(staffID)")
    stff_name=input("ENTER YOUR FIRST NAME:- ")
    mycursor.execute("INSERT INTO BOOKS [stff_name] VALUES(stff_name)")
elif stafforstudent.upper()=="STUDENT":
    studID=int(input("ENTER YOUR STUDENT_ID:- "))
    mycursor.execute("INSERT INTO BOOKS [stud_ID] VALUES(studID)")
    stf_name=input("ENTER YOUR FIRST NAME")
    mycursor.execute("INSERT INTO BOOKS [stf_name] VALUES(stf_name)")
else:
    print("WRONG INPUT CHECK YOUR DATA AGAIN!!!")