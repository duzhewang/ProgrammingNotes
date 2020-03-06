**SQL(Structured Query Language) tutorial**

- A database most often contains one or more tables. Each table is identified by a name (e.g. "Customers" or "Orders"). Tables contain records (rows) with data.
- SQL keywords are NOT case sensitive. 
- Semicolon is the standard way to separate each SQL statement in database systems that allow more than one SQL statement to be executed in the same call to the server.


*****************************************************
- SELECT: extracts data from a database
  - ``select column1, column2 from table_name ``: select column1 and column2 from the table. 
  - ``select * from table_name``: select all from the table. 

- SELECT DISTINCT: select distinct values from columns
   - ``SELECT DISTINCT column_name FROM table_name;``

- SELECT COUNT: count the number 
  - ``SELECT COUNT(DISTINCT column1) FROM table_name``: lists the number of different (distinct) values in column1
  - ``SELECT COUNT (column1) FROM table_name``: count the total numebr

- Where: 
  - ``SELECT column1, column2, ...FROM table_name WHERE condition;``

- And, or, not: 
  - ``SELECT column1, column2, ... FROM table_name WHERE condition1 AND condition2 AND condition3 ...;``
  - `` SELECT column1, column2, ... FROM table_name WHERE condition1 OR condition2 OR condition3 ...;``
  - `` SELECT column1, column2, ... FROM table_name WHERE NOT condition;``  
  
- Order by:
  - ``SELECT column1, column2, ... FROM table_name ORDER BY column1, column2, ... ASC|DESC;``

- Insert: used to insert new records in the table 
  - The first way specifies both the column names and the values to be inserted:
   `` INSERT INTO table_name (column1, column2, column3, ...)
      VALUES (value1, value2, value3, ...);
   ``   
   - If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query. However, make sure the order of the values is in the same order as the columns in the table. The INSERT INTO syntax would be as follows:
  `` INSERT INTO table_name
     VALUES (value1, value2, value3, ...);  
  ``
  
  
  
  
  
- UPDATE - updates data in a database

- DELETE - deletes data from a database

- INSERT INTO - inserts new data into a database

- CREATE DATABASE - creates a new database

- ALTER DATABASE - modifies a database

- CREATE TABLE - creates a new table

- ALTER TABLE - modifies a table

- DROP TABLE - deletes a table

- CREATE INDEX - creates an index (search key)

- DROP INDEX - deletes an index



