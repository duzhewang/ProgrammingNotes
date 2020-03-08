Problem: https://www.hackerrank.com/challenges/the-pads/problem

SQL: 
``Select Concat(Name, '(', left(Occupation, 1), ')') from Occupations order by Name; 
Select Concat('There are a total of', ' ', Count(*),' ',lower(occupation), 's.') from Occupations group by Occupation order by Count(Occupation) asc, Occupation asc;  
``
