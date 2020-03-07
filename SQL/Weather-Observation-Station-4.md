Problem: Let $N$ be the number of CITY entries in STATION, and let $N^{\prime}$ be the number of distinct CITY names in STATION; 
query the value of $N-N^{\prime}$ from STATION. In other words, find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.

SQL: ``Select Count(City)-Count(Distinct City) from Station;``
