Problem: https://www.hackerrank.com/challenges/placements/problem?h_r=next-challenge&h_v=zen


SQL:
```
Select T1.Name from 
(Select S.ID as ID, S.Name as Name, P.Salary as Salary, F.Friend_ID as Friend_ID from Students as S Join Packages as P on P.ID=S.ID
left join 
Friends as F on F.ID=S.ID) as T1
Join Packages as P2 on P2.ID=T1.Friend_ID
where T1.Salary<P2.Salary order by P2.Salary;
```
