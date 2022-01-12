Problem: 
Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. 
Then print these values as  space-separated integers.

SQL: 
```
SELECT top 1 months*salary as earnings, COUNT(*) FROM Employee GROUP BY months*salary order by months*salary desc;
```

reference: https://www.hackerrank.com/challenges/earnings-of-employees/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


MySQL:

```
Select months*salary as earnings, count(*) from Employee
group by earnings
order by earnings desc
limit 1
```


```
Select months*salary as total_earnings, count(*) from Employee
where months*salary=(select max(months*salary) from Employee)
group by months*salary; 

```
