**SQL(Structured Query Language) tutorial**

- A database most often contains one or more tables. Each table is identified by a name (e.g. "Customers" or "Orders"). Tables contain records (rows) with data.
- SQL keywords are NOT case sensitive. 
- Semicolon is the standard way to separate each SQL statement in database systems that allow more than one SQL statement to be executed in the same call to the server.


*****************************************************
- SELECT: extracts data from a database
  - ``select column1, column2 from table_name ``: select column1 and column2 from the table. 
  - ``select * from table_name``: select all from the table. 

- SELECT DISTINCT: select distinct values from columns
``SELECT DISTINCT column1, column2, ...FROM table_name;``

``SELECT COUNT(DISTINCT column1) FROM table_name;`` lists the number of different (distinct) values in column1


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



