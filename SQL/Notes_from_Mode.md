## 1. Basic SQL

### The SQL tutorial for data analysis

- What is SQL? a method for accessing data in database
- What is a database? A database is an organized collection of data


### SQL select

- There are two required ingredients in any SQL query: ```SELECT``` and ```FROM```—and they have to be in that order. ```SELECT``` indicates which columns you'd like to view, and ```FROM``` identifies the table that they live in.

- select every column in a table: ```select * from table_name```

- example of column names:

```
Select west as "West Region"
from tutorial.us_housing_units

```

### SQL limit

- example:

```
Select * from table_name
limit 100
```


### SQL where

- example:

```
select * from tutorial.us_housing_units
where month=1

```


### SQL comparison operators


- equal to: ```=```
- not equal to: ```<>``` or ```!=```
- greater than: ```>```
- less than: ```<```
- greater than or equal to: ```>=```
- less than or equal to: ```<=```


- If you're using an operator with values that are non-numeric, you need to put the value in single quotes


### SQL logical operators

- LIKE allows you to match similar values, instead of exact values.
- IN allows you to specify a list of values you'd like to include.
- BETWEEN allows you to select only rows within a certain range.
- IS NULL allows you to select rows that contain no data in a given column.
- AND allows you to select only rows that satisfy two conditions.
- OR allows you to select rows that satisfy either of two conditions.
- NOT allows you to select rows that do not match a certain condition.

### SQL like

- example:
```
SELECT *
  FROM tutorial.billboard_top_100_year_end
 WHERE "group" LIKE 'Snoop%'
```

The double quotes are a way of indicating that you are referring to the column name "group", not the SQL function. In general, putting double quotes around a word or phrase will indicate that you are referring to that column name.

- wildcards and ilike: In the type of SQL that Mode uses, LIKE is case-sensitive, meaning that the above query will only capture matches that start with a capital "S" and lower-case "noop." To ignore case when you're matching values, you can use the ILIKE command:

```
SELECT *
  FROM tutorial.billboard_top_100_year_end
 WHERE "group" ILIKE 'snoop%'
```

### SQL IN
