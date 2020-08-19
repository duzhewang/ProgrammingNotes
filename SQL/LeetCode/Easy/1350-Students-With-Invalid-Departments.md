Problem: 1350

SQL:
```
Select id, name from Students where id not in 
(Select S.id from Students as S Join Departments as D on D.id=S.department_id); 

```
