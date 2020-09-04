Problem: https://www.hackerrank.com/challenges/sql-projects/problem

SQL:

```
SELECT Start_Date, MIN(End_Date) FROM
(SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) as S,
(SELECT End_Date FROM Projects WHERE End_Date NOT IN (SELECT Start_Date FROM Projects)) as e 
WHERE Start_Date < End_Date
GROUP BY Start_Date
ORDER BY DATEDIFF(Day, Start_Date, MIN(End_Date)), Start_Date;
```

- Datediff: https://www.w3schools.com/sql/func_sqlserver_datediff.asp
