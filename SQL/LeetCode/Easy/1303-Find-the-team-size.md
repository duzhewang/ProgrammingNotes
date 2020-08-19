Problem: 1303

SQL:

```
Select E.employee_id, T.team_size from Employee as E Join 
(Select team_id, Count(team_id) as team_size from Employee group by team_id) as T
on T.team_id=E.team_id order by E.employee_id; 


```
