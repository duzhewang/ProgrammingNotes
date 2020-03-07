Problem: Query the two cities in STATION with the shortest and longest CITY names, 
as well as their respective lengths (i.e.: number of characters in the name). 
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

Sample Input:
Let's say that CITY only has four entries: DEF, ABC, PQRS and WXY

Sample Output:
``
ABC 3

PQRS 4
``

SQL: ``select top 1 City, LEN(City) City_Length from STATION order by City_Length ASC,City ASC;
select top 1 City, LEN(City) City_Length from STATION order by City_Length desc,City ASC``


Remark: use order by to order the city names and then use select top 1 to choose the desired one. 
