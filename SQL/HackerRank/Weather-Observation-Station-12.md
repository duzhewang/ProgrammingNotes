Problem: Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.

SQL: ``Select Distinct City from Station where City not like '[AEIOU]%' AND City not like '%[AEIOU]';``
