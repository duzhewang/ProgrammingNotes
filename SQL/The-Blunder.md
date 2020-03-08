Problem: Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, 
but did not realize her keyboard's 0 key was broken until after completing the calculation. 
She wants your help finding the difference between her miscalculation (using salaries with any zeroes removed), 
and the actual average salary. Write a query calculating the amount of error, and round it up to the next integer.


SQL: ``SELECT round(AVG(salary) - AVG(cast(REPLACE(salary, '0', '') as int)), 0)+1 AS avg_salary FROM employees;``


- Round(number, n): round the number to n decimal 
- REPLACE('SQL Tutorial', 'T', 'M'): replace T by M
- CAST(25.65 AS int): cast a value into an integer 
