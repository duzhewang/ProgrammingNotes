Problem: https://www.hackerrank.com/challenges/asian-population/problem

SQL: 
``SELECT sum(i.population) FROM CITY AS i 
JOIN COUNTRY AS o ON i.COUNTRYCODE=o.CODE WHERE o.CONTINENT='Asia';
``

Join function: https://www.w3schools.com/sql/sql_join.asp
