Problem: LeetCode 1378

SQL:
```
Select Em.unique_id, E.name from Employees as E 
left join EmployeeUNI as Em on Em.id=E.id;
```
