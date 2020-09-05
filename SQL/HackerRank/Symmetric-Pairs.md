Problem: https://www.hackerrank.com/challenges/symmetric-pairs/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

SQL: 

```
SELECT f1.X, f1.Y FROM Functions AS f1 
WHERE f1.X = f1.Y group by f1.X, f1.Y having count(*)>1
UNION
SELECT f1.X, f1.Y FROM Functions AS f1, Functions AS f2
WHERE f1.X <> f1.Y AND f1.X = f2.Y AND f1.Y = f2.X AND f1.X < f2.X
ORDER BY f1.X;
```


- Union: https://www.w3schools.com/sql/sql_union.asp
