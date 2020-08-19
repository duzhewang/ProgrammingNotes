Problem: Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

SQL: ``Select Distinct City from Station where City not like '[AEIOU]%[AEIOU]';``
