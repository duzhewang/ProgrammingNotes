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
  
- Null: 
  - ``SELECT column_names FROM table_name WHERE column_name IS NULL; ``
  
  
- UPDATE: the UPDATE statement is used to modify the existing records in a table.
  ``UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;``

- DELETE: The DELETE statement is used to delete existing records in a table.
  - ``DELETE FROM table_name WHERE condition;``
  - ``DELETE FROM table_name;``

- Select Top: select the top number of records 
   `` SELECT TOP number column_name(s) FROM table_name WHERE condition;``

- Min and Max: 
  - ``SELECT MIN(column_name) as Some_name FROM table_name  WHERE condition;``
  - ``SELECT MAX(column_name) FROM table_name WHERE condition;``

- Count, Average and Sum:
  - ``SELECT COUNT(column_name) FROM table_name WHERE condition;``
  - ``SELECT AVG(column_name) FROM table_name WHERE condition;``
  - ``SELECT SUM(column_name) FROM table_name WHERE condition;``
  
  
- Like: The LIKE operator is used in a WHERE clause to search for a specified pattern in a column. There are two wildcards often used in conjunction with the LIKE operator:
  - %: The percent sign represents zero, one, or multiple characters
  - _: The underscore represents a single character
  - ``SELECT column1, column2, ... FROM table_name WHERE columnN LIKE pattern;`` 
  - https://www.w3schools.com/sql/sql_like.asp


- IN: The IN operator allows you to specify multiple values in a WHERE clause. The IN operator is a shorthand for multiple OR conditions.
  ``SELECT column_name FROM table_name WHERE column_name IN (value1, value2, ...);``


- Between: The BETWEEN operator selects values within a given range. The values can be numbers, text, or dates. The BETWEEN operator is inclusive: begin and end values are included. 
  ``SELECT column_name(s) FROM table_name WHERE column_name BETWEEN value1 AND value2;``
  
- Aliases: SQL aliases are used to give a table, or a column in a table, a temporary name. Aliases are often used to make column names more readable. An alias only exists for the duration of the query.  
  ``SELECT column_name AS alias_name FROM table_name;``  
  
- Left join, Right join, Inner join, Full join: https://www.w3schools.com/sql/sql_join.asp

- Comments: 
  - Single-line comments: Single line comments start with --. Any text between -- and the end of the line will be ignored (will not be executed).  
  - Multiple-line comments: Multi-line comments start with /* and end with */. Any text between /* and */ will be ignored.




---------------------------------
## SQL interview questions 

1. What is Database?

A database is an organized collection of data, stored and retrieved digitally from a remote or local computer system. Databases can be vast and complex, and such databases are developed using fixed design and modeling approaches.

2. What is DBMS?

DBMS stands for Database Management System. DBMS is a system software responsible for the creation, retrieval, updation and management of the database. It ensures that our data is consistent, organized and is easily accessible by serving as an interface between the database and its end users or application softwares.

3. What is RDBMS? How is it different from DBMS?

RDBMS stands for Relational Database Management System. The key difference here, compared to DBMS, is that RDBMS stores data in the form of a collection of tables and relations can be defined between the common fields of these tables. Most modern database management systems like MySQL, Microsoft SQL Server, Oracle, IBM DB2 and Amazon Redshift are based on RDBMS.


4. What is SQL?

SQL stands for Structured Query Language. It is the standard language for relational database management systems. It is especially useful in handling organized data comprised of entities (variables) and relations between different entities of the data.


5. What is the difference between SQL and MySQL?

SQL is a standard language for retrieving and manipulating structured databases. On the contrary, MySQL is a relational database management system, like SQL Server, Oracle or IBM DB2, that is used to manage SQL databases.


6. What are Tables and Fields?

A table is an organized collection of data stored in the form of rows and columns. Columns can be categorized as vertical and rows as horizontal. **The columns in a table are called fields while the rows can be referred to as records.**


7. What are Constraints in SQL?

Constraints are used to specify the rules concerning data in the table. It can be applied for single or multiple fields in an SQL table during creation of table or after creationg using the ALTER TABLE command. The constraints are:

NOT NULL - Restricts NULL value from being inserted into a column.
CHECK - Verifies that all values in a field satisfy a condition.
DEFAULT - Automatically assigns a default value if no value has been specified for the field.
UNIQUE - Ensures unique values to be inserted into the field.
INDEX - Indexes a field providing faster retrieval of records.
PRIMARY KEY - Uniquely identifies each record in a table.
FOREIGN KEY - Ensures referential integrity for a record in another table.

8. What is a Primary Key?

The PRIMARY KEY constraint uniquely identifies each row in a table. It must contain UNIQUE values and has an implicit NOT NULL constraint.
A table in SQL is strictly restricted to have one and only one primary key, which is comprised of single or multiple fields (columns).


9. What is a UNIQUE constraint?

A UNIQUE constraint ensures that all values in a column are different. This provides uniqueness for the column(s) and helps identify each row uniquely. Unlike primary key, there can be multiple unique constraints defined per table. The code syntax for UNIQUE is quite similar to that of PRIMARY KEY and can be used interchangeably.

10. What is a Foreign Key?

A FOREIGN KEY comprises of single or collection of fields in a table that essentially refer to the PRIMARY KEY in another table. Foreign key constraint ensures referential integrity in the relation between two tables.
The table with the foreign key constraint is labelled as the child table, and the table containing the candidate key is labelled as the referenced or parent table.

11. What is a Join? List its different types.

The SQL Join clause is used to combine records (rows) from two or more tables in a SQL database based on a related column between the two.

12. What is a Self-Join?

A self JOIN is a case of regular join where a table is joined to itself based on some relation between its own column(s). Self-join uses the INNER JOIN or LEFT JOIN clause and a table alias is used to assign different names to the table within the query.

13. What is a Cross-Join?

Cross join can be defined as a cartesian product of the two tables included in the join. The table after join contains the same number of rows as in the cross-product of number of rows in the two tables. If a WHERE clause is used in cross join then the query will work like an INNER JOIN.























