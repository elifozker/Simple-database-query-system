# Simple-database-query-system


Problem: Design a simple database query system. The system must accept a CSV file (students.csv) as input as the initial database. After initial loading of the file, the records must be sorted by their index. The query will be given in SQL with a restricted command set for simplicity (see below for details). The resulting data set (result of the query) must be stored as a JSON file.


Methods:
• You must use the Python programming language and your code must be in a single PY file. We recommend Anaconda Navigator package with Spyder IDE.
o You can use another IDE, but we will not help with problems arising from the selection of a different IDE.
o You can use Jupyter Notebook (Also in Anaconda package) to test and debug your code, BUT your final submission upload must be in stand-alone Python code with PY extension.

• You can use any Python library shown in the course, libraries for reading CSV and writing JSON files. However, you must:
o Install the libraries yourself by following the installation procedures in the webpages of the libraries.
o NOT use a library for query parsing.
o You must hold the records in a sorteddict defined in blist library (You must
install the blist1 library). A sorteddict2 uses a tree structure and works faster on range queries than a regular Python dictionary. You can sort and search using sorteddict.
o If you are unsure of whether you can use a new library you find, write a post in the Forum and get our confirmation.
• Accept the query from the user and give an error message if the query doesn’t fit the format of simplified SQL given below.
Simplified SQL: It has the following form:
SELECT {ALL|column_name} FROM STUDENTS WHERE {column_name|=,!=,<,>,<=,>=,!<,!>,AND,OR3} ORDER BY{ASC|DSC}
INSERT INTO STUDENT VALUES(val1,val2,val3,...)
DELETE FROM STUDENT WHERE {column_name|=,!=,<,>,<=,>=,!<,!>,AND,OR }5 exit
Examples:
SELECT name,lastname6 FROM STUDENTS WHERE grade !< 40 ORDER BY ASC
SELECT name FROM STUDENTS WHERE grade > 40 AND name = ‘John’ ORDER BY DSC
INSERT INTO STUDENT VALUES(15000,Ali,Veli,ali.veli@spacex.com,20)
DELETE FROM STUDENT WHERE name = ‘John’ and grade <= 20
