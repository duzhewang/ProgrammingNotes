Problem: 613

SQL: 

```
Select min(abs(p1.x-p2.x)) as shortest from point as p1, point as p2 where p1.x<>p2.x; 

```
