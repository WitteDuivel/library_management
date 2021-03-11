import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="2zkNKcz&EOZaRjc$",database="library")
mycursor=mydb.cursor()
studID=input("ENTER YOUR STUDENT ID:- ")
#TODO QUERY TO ADD THE stud_ID INTO THE TABLE STUDENT
mycursor.execute("INSERT INTO STUDENT [stud_ID] VALUES(studID)")
stf_name=input("ENTER YOUR FIRST NAME:- ")
#TODO QUERY TO ADD THE stfname INTO THE TABLE STUDENT
mycursor.execute("INSERT INTO STUDENT [stfname] VALUES(stf_name)")
stl_name=input("ENTER YOUR LAST NAME:- ")
#TODO QUERY TO ADD THE stlname INTO THE TABLE STUDENT
mycursor.execute("INSERT INTO STUDENT [stlname] VALUES(stl_name)")
st_course=input("ENTER YOUR COURSE:- ")
#TODO QUERY TO ADD THE stcourse INTO THE TABLE STUDENT
mycursor.execute("INSERT INTO STUDENT [stcourse] VALUES(st_course)")
st_year=input("ENTER THE YEAR YOU GOT ADMISSION IN:- ")
#TODO QUERY TO ADD THE styear INTO THE TABLE STUDENT
mycursor.execute("INSERT INTO STUDENT [styear] VALUES(st_year)")
st_contact=int(input("ENTER YOUR CONTACT NUMBER:-"))
#TODO QUERY TO ADD THE stcontact INTO THE TABLE STUDENT
mycursor.execute("INSERT INTO STUDENT [stcontract] VALUES(st_contract)")
st_age=int(input("ENTER YOUR AGE:-"))
#TODO QUERY TO ADD THE stage INTO THE TABLE STUDENT
mycursor.execute("INSERT INTO STUDENT [stage] VALUES(st_age)")
st_birthdate=input("ENTER YOUR BIRTH DATE IN (YYYY-MM-DD) FORMAT:- ")
#TODO QUERY TO ADD THE stbirthdate INTO THE TABLE STUDENT
mycursor.execute("INSERT INTO STUDENT [stbirthdate] VALUES(st_birthdate)")
st_gender=input("ENTER YOUR GENDER:- ")
#TODO QUERY TO ADD THE stgender INTO THE TABLE STUDENT
mycursor.execute("INSERT INTO STUDENT [stgender] VALUES(st_gender)")
