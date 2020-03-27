Problem: 627

SQL: 

```
Update salary 
Set 
  sex= case sex
         when 'm' then 'f'
         else 'm'
        end;  

```
