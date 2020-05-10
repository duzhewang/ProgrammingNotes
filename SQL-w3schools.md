# SQL syntax

- Database Tables

A database most often contains one or more tables. Each table is identified by a name (e.g. "Customers" or "Orders"). Tables contain records (rows) with data.

- SQL Statements

Most of the actions you need to perform on a database are done with SQL statements. SQL keywords are NOT case sensitive: select is the same as SELECT.

Some database systems require a semicolon at the end of each SQL statement. Semicolon is the standard way to separate each SQL statement in database systems that allow more than one SQL statement to be executed in the same call to the server.


# The SQL SELECT Statement

The SELECT statement is used to select data from a database. The data returned is stored in a result table, called the result-set.

SELECT Syntax: 

```
SELECT column1, column2, ...
FROM table_name;
```

Here, column1, column
2, ... are the field names of the table you want to select data from. If you want to select all the fields available in the table, use the following syntax:
```
SELECT * FROM table_name
```

# The SQL SELECT DISTINCT Statement

The SELECT DISTINCT statement is used to return only **distinct (different)** values. Inside a table, a column often contains many duplicate values; and sometimes you only want to list the different (distinct) values.

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








