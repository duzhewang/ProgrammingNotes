Problem: https://www.hackerrank.com/challenges/the-report/problem

MySQL: 
```
Select if (g.Grade>=8,Name, NULL), Grade, Marks from Students as S Join Grades as g on S.Marks between g.Min_Mark and g.Max_Mark order by Grade desc, Name, Marks;  
```


SQL: 
```
Select case when G.grade<8 then NULL
            else S.name
       end, G.grade, S.marks from Students as S, Grades as G
where S.marks>=G.min_mark and S.marks<=G.max_mark
order by G.grade desc, S.name; 
```
