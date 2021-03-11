import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="2zkNKcz&EOZaRjc$",database="library")
mycursor=mydb.cursor()
bookID=int(input("ENTER THE BOOK_ID:- "))
#TODO QUERY TO ADD THE book_ID INTO THE TABLE BOOK
mycursor.execute("INSERT INTO BOOKS [book_ID] VALUES(bookID)")
bk_title=input("ENTER THE BOOK TITLE:- ")
#TODO QUERY TO ADD THE bktitle INTO THE TABLE BOOK
mycursor.execute("INSERT INTO BOOKS [bktitle] VALUES(bk_title)")
bk_edition=input("ENTER THE BOOK EDITION:- ")
#TODO QUERY TO ADD THE bkedition INTO THE TABLE BOOK
mycursor.execute("INSERT INTO BOOKS [bkedition] VALUES(bk_edition)")
bk_author=input("ENTER THE NAME OF THE AUTHOR OF THE BOOK:- ")
#TODO QUERY TO ADD bkauthor INTO THE TABLE BOOK
mycursor.execute("INSERT INTO BOOKS [bkauthor] VALUES(bk_author)")
bk_pulisher=input("ENTER THE NAME OF THE NAME OF THE PUBLISHER OF THE BOOK:- ")
#TODO QUERY TO ADD bkpublisher INTO THE TABLE BOOK
mycursor.execute("INSERT INTO BOOKS [bkpublisher] VALUES(bk_publisher)")
bk_copies=int(input("ENTER THE NUMBER OF BOOKS PRESENT:- "))
#TODO QUERY TO ADD bkcopies INTO THE TABLE BOOK
mycursor.execute("INSERT INTO BOOKS [bkcopies] VALUES(bk_copise)")
bksource=input("ENTER THE SOURCE OF THE BOOK:- ")
#TODO QUERY TO ADD bksource INTO THE TABLE BOOK
mycursor.execute("INSERT INTO BOOKS [bk_source] VALUES(bksource)")
bkcost=int(input("ENTER THE COST OF THE BOOK:- "))
#TODO QUERY TO ADD bk_cost INTO THE TABLE BOOK
mycursor.execute("INSERT INTO BOOKS [bk_cost] VALUES(bkcost)")
bkremarks=input("ENTER ANY REMARKS YOU WANT TO ADD FOR THIS BOOK:- ")
#TODO QUERY TO ADD bk_remarks INTO THE TABLE BOOK
mycursor.execute("INSERT INTO BOOKS [bk_remarks] VALUES(bkremarks)")
