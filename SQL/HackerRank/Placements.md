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

```
Select T.name from
(Select S.Id, S.name, P.Salary, F.friend_id from Students as S
join Packages as P
on S.id=P.id
join Friends as F
on F.id=S.id) as T
join Packages as P
on P.id=T.friend_id
where P.salary>T.salary
order by P.salary; 
```


MySQL:

```
Select S.Name from Friends as F
join Packages as P1
on F.ID=P1.ID
join Packages as P2
on F.Friend_ID=P2.ID
join Students as S
on S.ID=F.ID
where P2.salary>P1.salary
order by P2.salary



```
