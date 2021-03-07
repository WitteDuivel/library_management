CREATE DATABASE library

CREATE TABLE BOOK( book_ID VARCHAR, bktitle VARCHAR, bkedition VARCHAR, bkauthor VARCHAR, bkpublisher VARCHAR, bkcopies INT, bk_source VARCHAR, bk_cost INT, bk_remarks VARCHAR )

CREATE TABLE USERS( staff_ID VARCHAR, stffname CHAR, stfflname CHAR, stffcontactnumber INT, stfemail VARCHAR, stfaddress VARCHAR, stfpassword VARCHAR, stftype VARCHAR )

CREATE TABLE BookReturnRecords( Borrowers_ID VARCHAR, book_ID VARCHAR, bktitle VARCHAR, stud_ID VARCHAR, stfname CHAR, staff_ID VARCHAR, stffname CHAR, studentNOcopies VARCHAR, releaseDate DATE, duedate DATE, bkdatereturn DATE )

CREATE TABLE STUDENTS( stud_ID VARCHAR PRIMARY KEY , stfname VARCHAR, stcourse VARCHAR, styear VARCHAR, stcontract VARCHAR, stage VARCHAR, stbirthdate VARCHAR, stgender VARCHAR )

CREATE TABLE borrowers_records( Borrowers_ID VARCHAR, book_ID VARCHAR, bktitle VARCHAR, stud_ID VARCHAR, stffname CHAR, staff_ID VARCHAR, studentNOcopies VARCHAR, releaseDate DATE, dueDATE DATE, )
