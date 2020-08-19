Problem: Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.

SQL: ``Select Distinct City from Station where City Not like "%a" and City not like "%e" and City not like "%i" and City not like "%o" and City not like "%u";``
