import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="2zkNKcz&EOZaRjc$",database="library")
mycursor=mydb.cursor()
staff=int(input("ENTER YOUR STAFF_ID:- "))
#TODO QUERY TO ADD staff_ID INTO THE TABLE USERS
mycursor.execute("INSERT INTO USERS [staff_ID] VALUES(staff)")
stff_name=input("ENTER YOUR FIRST NAME:- ")
#TODO QUERY TO ADD THE stffname INTO THE TABLE USERS
mycursor.execute("INSERT INTO USERS [stffname] VALUES(staff_name)")
stffl_name=input("ENTER YOUR LAST NAME- ")
#TODO QUERY TO ADD THE stfflname INTO THT TABLE USERS
mycursor.execute("INSERT INTO USERS stfflname] VALUES(stffl_name)")
stffcontact=input("ENTER YOUR CONTACT NUMBER:- ")
#TODO QUERY TO ADD THE stffcontactnumber INTO THE TABLE USERS
mycursor.execute("INSERT INTO USERS [staffcontactnumber] VALUES(staffcontact)")
stf_email=input("ENTER YOUR EMAIL_ID:- ")
#TODO QUERY TO ADD THE stfemail INTO THE TABLE USERS
mycursor.execute("INSERT INTO USERS [stfemail] VALUES(stf_email)")
stf_address=input("ENTER YOUR HOME ADDRESS:- ")
#TODO QUERY TO ADD THE stfaddress INTO THE TABLE USERS
mycursor.execute("INSERT INTO USERS [stfaddress] VALUES(stf_address)")
stf_password=input("ENTER YOUR PASSWORD FOR THE NEW ACCOUNT:- ")
#TODO QUERY TO ADD THE stfpassword INTO THE TABLE USERS
mycursor.execute("INSERT INTO USERS [stfpassword] VALUES(stf_password)")
stf_type=input("ON HOLD THIS IS JUST A PLACEHOLDER TEXT:- ")
#TODO QUERY TO ADD THE stftype INTO THE TABLE USERS
mycursor.execute("INSERT INTO USERS [stftype] VALUES(stf_type)")
