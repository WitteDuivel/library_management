import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="2zkNKcz&EOZaRjc$",database="library")
mycursor=mydb.cursor()
BorrowersID=int(input("ENTER YOUR BORROWER_ID:- "))
mycursor.execute("INSERT INTO BookReturnRecords [Borrowers_ID] VALUES(BorrowersID)")
bookID=input("ENTER BOOK_ID:- ")
mycursor.execute("INSERT INTO BookReturnRecords [Book_ID] VALUES(bookID)")
bk_title=input("ENTER THE BOOK'S TITLE:- ")
mycursor.execute("INSERT INTO BookReturnRecords [bktitle] VALUES(bk_title)")
stafforstudent=input("ARE YOU A STAFF OR A STUDENT? (STAFF/STUDENT)")
if stafforstudent.upper()=="STAFF":
    staffID=int(input("ENTER YOUR STAFF_ID:- "))
    mycursor.execute("INSERT INTO BookReturnRecords [stud_ID] VALUES(studID)")
    stff_name=input("ENTER YOUR FIRST NAME:- ")
    mycursor.execute("INSERT INTO BookReturnRecords [stffname] VALUES(stff_name)")
elif stafforstudent.upper()=="STUDENT":
    studID=int(input("ENTER YOUR STUDENT_ID:- "))
    mycursor.execute("INSERT INTO BookReturnRecords [stud_ID] VALUES(studID)")
    stf_name=input("ENTER YOUR FIRST NAME")
    mycursor.execute("INSERT INTO BookReturnRecords [stfname] VALUES(stf_name)")
else:
    print("WRONG INPUT CHECK YOUR DATA AGAIN!!!")
release_Date=input("ENTER THE RELEASE DATE:- ")
mycursor.execute("INSERT INTO BookReturnRecords [releaseDate] VALUES(release_Date)")

due_date=input("ENTER THE DUE DATE:- ")
mycursor.execute("INSERT INTO BookReturnRecords [duedate] VALUES(due_date)")
bk_datereturn=input("ENTER THE RETURN DATE:- ")
mycursor.execute("INSERT INTO BookReturnRecords [bkdatereturn] VALUES(bk_datereturn)")