# SQL syntax

- Database Tables: A database most often contains one or more tables. Each table is identified by a name. Tables contain records (rows) with data.

- SQL Statements: Most of the actions you need to perform on a database are done with SQL statements. **SQL keywords are NOT case sensitive**.

- Some database systems require a semicolon at the end of each SQL statement. Semicolon is the standard way to separate each SQL statement in database systems that allow more than one SQL statement to be executed in the same call to the server.

- Some of the most important SQL commands:
  - ```Select```: extracts data from a database
  - ```Update```: updates data in a database
  - ```Delete```: deletes data from a database
  - ```Insert into```: inserts new data into a database
  - ```Create database```: creates a new database
  - ```alter database```: modifies a database
  - ```create table```: creates a new table
  - ```alter table```: modifies a table
  - ```drop table```: deletes a table
  - ```create index```: creates an index
  - ```drop index```: deltes an index


  | Command       | Syntax            | Function |
  |---------------|-------------------|----------|
  |    Select     |  Select column1, column2,... from table_name| select data from a database |       
  |  Select distinct       |   Select distinct column1, column2 from table_name      | return only distinct values         |         
  |  where       | select column1, column2,... from table_name where condition;       | the where clause is used to extract only those records that fulfill a specified condition          |
  |         























# The SQL SELECT Statement

- The ```SELECT``` statement is used to select data from a database. The data returned is stored in a result table, called the result-set.

- Syntax:

```
SELECT column1, column2, ...
FROM table_name;
```

Here, column1, column2, ... are the field names of the table you want to select data from. If you want to select all the fields available in the table, use the following syntax:

```
SELECT * FROM table_name
```

# The SQL SELECT DISTINCT Statement

- The SELECT DISTINCT statement is used to return only **distinct (different)** values. Inside a table, a column often contains many duplicate values; and sometimes you only want to list the different (distinct) values.

SELECT DISTINCT Syntax:
```
SELECT DISTINCT column1, column2, ...
FROM table_name;
```


# The SQL WHERE Clause

The WHERE clause is used to filter records. The WHERE clause is used to extract only those records that fulfill a specified condition.

WHERE Syntax:

```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```


Operators in The WHERE Clause:

```
=	Equal
>	Greater than
<	Less than
>=	Greater than or equal
<=	Less than or equal
<>	Not equal. Note: In some versions of SQL this operator may be written as !=
BETWEEN	Between a certain range
LIKE	Search for a pattern
IN	To specify multiple possible values for a column
```

# The SQL AND, OR and NOT Operators

The WHERE clause can be combined with AND, OR, and NOT operators.

The AND and OR operators are used to filter records based on more than one condition. The AND operator displays a record if all the conditions separated by AND are TRUE. The OR operator displays a record if any of the conditions separated by OR is TRUE. The NOT operator displays a record if the condition(s) is NOT TRUE.

AND Syntax:

```
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
```

OR Syntax:
```
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
```
NOT Syntax:
```
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
```


# The SQL ORDER BY Keyword

The ORDER BY keyword is used to sort the result-set in ascending or descending order.

The ORDER BY keyword sorts the records in ascending order by default. To sort the records in descending order, use the DESC keyword.

ORDER BY Syntax:

```
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

# The SQL INSERT INTO Statement

The INSERT INTO statement is used to insert new records in a table.

INSERT INTO Syntax:
```
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query. However, make sure the order of the values is in the same order as the columns in the table. The INSERT INTO syntax would be as follows:

```
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```

# What is a NULL Value?

A field with a NULL value is a field with no value. If a field in a table is optional, it is possible to insert a new record or update a record without adding a value to this field. Then, the field will be saved with a NULL value.

Note: A NULL value is different from a zero value or a field that contains spaces. A field with a NULL value is one that has been left blank during record creation!

How to Test for NULL Values?

IS NULL Syntax:
```
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
```
IS NOT NULL Syntax:
```
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
```

# The SQL UPDATE Statement

The UPDATE statement is used to modify the existing records in a table.

UPDATE Syntax:
```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

# The SQL DELETE Statement

The DELETE statement is used to delete existing records in a table.

DELETE Syntax:
```
DELETE FROM table_name WHERE condition;
```

# The SQL SELECT TOP Clause

The SELECT TOP clause is used to specify the number of records to return. The SELECT TOP clause is useful on large tables with thousands of records. Returning a large number of records can impact performance.

SQL Server / MS Access Syntax:
```
SELECT TOP number|percent column_name(s)
FROM table_name
WHERE condition;
```
MySQL Syntax:
```
SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;
```


# The SQL MIN() and MAX() Functions

The MIN() function returns the smallest value of the selected column. The MAX() function returns the largest value of the selected column.

MIN() Syntax:
```
SELECT MIN(column_name)
FROM table_name
WHERE condition;
```
MAX() Syntax:
```
SELECT MAX(column_name)
FROM table_name
WHERE condition;
```

# The SQL COUNT(), AVG() and SUM() Functions

The COUNT() function returns the number of rows that matches a specified criterion.

The AVG() function returns the average value of a numeric column.

The SUM() function returns the total sum of a numeric column.

COUNT() Syntax:
```
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
```
AVG() Syntax:
```
SELECT AVG(column_name)
FROM table_name
WHERE condition;
```
SUM() Syntax:
```
SELECT SUM(column_name)
FROM table_name
WHERE condition;
```

# The SQL LIKE Operator

The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

There are two wildcards often used in conjunction with the LIKE operator:

```%``` - The percent sign represents zero, one, or multiple characters

```_``` - The underscore represents a single character
Note: M

# SQL wildcard: https://www.w3schools.com/sql/sql_wildcards.asp


# The SQL IN Operator

The IN operator allows you to specify multiple values in a WHERE clause.

The IN operator is a shorthand for multiple OR conditions.

IN Syntax:
```
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);
```
or:

```
SELECT column_name(s)
FROM table_name
WHERE column_name IN (SELECT STATEMENT);
```


# The SQL BETWEEN Operator

The BETWEEN operator selects values within a given range. The values can be numbers, text, or dates.

The BETWEEN operator is inclusive: begin and end values are included.

BETWEEN Syntax:
```
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

# SQL Aliases

SQL aliases are used to give a table, or a column in a table, a temporary name.

Aliases are often used to make column names more readable. An alias only exists for the duration of the query.

Alias Column Syntax:
```
SELECT column_name AS alias_name
FROM table_name;
```

# Different Types of SQL JOINs

Here are the different types of the JOINs in SQL:

- (INNER) JOIN: Returns records that have matching values in both tables

- LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table

- RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table

- FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table

INNER JOIN Syntax:
```
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```

LEFT JOIN Syntax:
```
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```

RIGHT JOIN Syntax:
```
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
```

FULL OUTER JOIN Syntax:
```
SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2
ON table1.column_name = table2.column_name
WHERE condition;
```


Self JOIN Syntax:
```
SELECT column_name(s)
FROM table1 T1, table1 T2
WHERE condition;
```

# The SQL UNION Operator

The UNION operator is used to combine the result-set of two or more SELECT statements. Each SELECT statement within UNION must have the same number of columns. The columns must also have similar data types. The columns in each SELECT statement must also be in the same order.

UNION Syntax:
```
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
```
UNION ALL Syntax:
```
SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;
```

# The SQL GROUP BY Statement

The GROUP BY statement groups rows that have the same values into summary rows, like "find the number of customers in each country".

The GROUP BY statement is often used with aggregate functions (COUNT, MAX, MIN, SUM, AVG) to group the result-set by one or more columns.

GROUP BY Syntax:

```
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);
```

# The SQL HAVING Clause
The HAVING clause was added to SQL because **the WHERE keyword could not be used with aggregate functions.**

HAVING Syntax:
```
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
```

# The SQL EXISTS Operator
The EXISTS operator is used to test for the existence of any record in a subquery.

The EXISTS operator returns true if the subquery returns one or more records.

EXISTS Syntax:
```
SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition);
```

# The SQL CASE Statement

The CASE statement goes through conditions and returns a value when the first condition is met (like an IF-THEN-ELSE statement). So, once a condition is true, it will stop reading and return the result. If no conditions are true, it returns the value in the ELSE clause.

If there is no ELSE part and no conditions are true, it returns NULL.

CASE Syntax:
```
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END;
```
