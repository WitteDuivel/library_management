#NOTE
#N ask the user if they are a staff member or a student
#N verify their id accroding to what they are(staff_ID for staff members and stud_ID for students)
#? FIRST FOR THE STUDENT USERS
#N if the stud_id is verfied move ahead
#N if the stud_id is not already registered than register the student and then move ahead
#N for verified students ask if they want to return the book or want to borrow a book
#N if they want to borrow the book ask for the bktitle and verify if it exists in the BOOK and inform the student accordingly
#N take all the necessary information according to the table borrowers_records 
#N update the table BOOK
#N if they want to return the book take all the necessary information according to the table BookReturnRecords
#N update the table BOOK
#? NOW COMING TO THE STAFF USERS
#N if the staff_ID si verified move ahead
#N if the staff_ID is not already registered than register the staff and then move ahead
#N ask them if they want to manage books or manage their data
#N if they want to manage books ask them if they want to borrow the books or add the books
#? FIRST IF THEY WANT TO MANAGE THE BOOKS
#N ask for the details of the book they want to add
#N update the table BOOK
#? NOW COMING TO THE PART WHERE THEY WANT TO BORROW THE BOOKS 
#N use the same query as student
#? NOW IF THEY WANT TO MANAGE THEIR DATA
#N ask for their login credentials
#N if they are verified move ahead
#N ask what do they want to update
#N update table USERS accordigly
stforstud=input("ARE YOU A STAFF MEMBER OR A STUDENT? (STAFF/STUDENT)")
if stforstud=="STAFF":
    print("YOU ARE WELCOME!!!")
    neworold=input("ARE YOU A REGISTERED STAFF MEMBER? (YES/NO)")
    if neworold=="YES":
        staff_ID=int(input("PLEASE ENTER YOUR STAFF_ID:- "))
        #TODO QUERY FOR CHECKING IF THE ID ENTERED EXISTS OR NOT
        #TODO IF EXISTS THEN AN IF STATEMENT TO VERIFY PASSWORD
        #TODO IF DOESN'T EXIST ASK IF THEY WANT TO REGISTER OR WANT TO LEAVE
        dataorbook=input("DO YOU WANT TO MANAGE YOUR DATA OR WANT TO MANAGE THE LIBRARY? (DATA/LIBRARY)")
        if dataorbook=="DATA":
            wholeorpart=input("DO YOU WANT TO CHANGE A PARTICULAR DATA OR WANT TO UPDATE YOUR WHOLE RECORDS? (SOME/WHOLE)")
            if wholeorpart=="SOME":
                which=input("WHICH OF THE FOLLOWING DATA YOU WANT TO UPDATE? ( staff_ID/stffname/stfflname/stffcontactnumber/stfemail/stfaddress/stfpassword/stftype)")
                #TODO QUERY TO UPDATE THE CHOSEN RECORDS ACCRODINGLY
            elif wholeorpart=="WHOLE":
                #TODO QUERY TO UPDATE THE WHOLE RECORD OF THE CURRENT USER
                pass
            else:
                print("WRONG INPUT")
        elif dataorbook=="BOOK":
            addormanage=input("DO YOU WANT TO ADD THE BOOK OR MANAGE THE DATA OF THE CURRENT BOOKS? (ADD/MANAGE)")
            if addormanage=="ADD":
                #TODO TO ADD A NEW BOOK IN THE DATABASE AND UPDATE THE TABLE BOOK
                pass
            elif addormanage=="MANAGE":
                #TODO QUERY TO MANAGE THE TABLE BOOK ACCRODING TO USERS NEED
                pass
            else:
                print("WRONG INPUT")
    elif neworold=="NO":
        registerornot=input("DO YOU WANT TO REGISTER AS A NEW STAFF MEMBER OF THIS LIBRARY? (YES/NO)")
        if registerornot=="YES":
            #TODO QUERY TO ASK FOR THE REQUIRED INFORMATION NEEDED TO REGISTER THE NEW STAFF MEMBER ACCORDING TO THE TABLE USERS
            pass
        elif registerornot=="NO":
            print("TRY TO NOT WASTE TIME OF OURS AND OTHERS, THANK YOU!!!")
        else:
            print("WRONG INPUT, CHECK THE DATA AGAIN. POSSIBLE ERRORS MAY INCLUDE NOT SPELLING CORRECTLY OR DIFFERENT CASE OF THE LETTERS RATHER THAN CAPS. TRY AGAIN KEEPING THERE IN MIND")
    else:
        print("WRONG INPUT, CHECK AGAIN IF YOU HAVE SPELLT IT CORRECTLY AND IN THE UPPER CASE")
elif stforstud=="STUDENT":
    print("WELCOME PRECIOUS FUTURE OF THIS EARTH :)")
    existingornot=input("ARE YOU A REGISTERED STUDENT? (YES/NO)")
    if existingornot=="YES":
        stud_ID=int(input("KINDLY ENTER YOUR STUDENT_ID PLEASE:- "))
        #TODO QUERY TO VERIFY THE AVAILIBILITY OF THE STUDENT IN THE DATABASE
        #TODO IF THE STUDENT DOESN'T EXIST ASK THE STUDENT TO EITHER REGISTER OR LEAVE
    elif existingornot=="NO":
        registerornot_=input("DO YOU WANT TO REGISTER YOUR RECORDS IN THIS LIBRARY,")
        if registerornot_=="YES":
            #TODO QUERY TO ADD THE STUDENT INTO THE DATABASE AND UPADATE THE TABLE STUDENT
            pass
        elif registerornot_=="NO":
            print("EITHER REGISTER INTO YOURSELF INTO THE DATABASE OR YOU WON'T BE ABLE TO ACCESS THE LIBRARY")
            #TODO ADD AN OPTION TO GO BACK TO THE REGISTERING PART
        else:
            print("WRONG INPUT CHECK AGAIN")
    else:
        print("WRONG INPUT CHECK AGAIN")
else:
    print("WRONG INPUT, CHECK AGAIN IF YOU HAVE SPELLT IT CORRECTLY AND IN THE UPPER CASE")
