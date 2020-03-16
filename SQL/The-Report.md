Problem: https://www.hackerrank.com/challenges/the-report/problem

MySQL: 
``
Select if (g.Grade>=8,Name, NULL), Grade, Marks from Students as S Join Grades as g on S.Marks between g.Min_Mark and g.Max_Mark order by Grade desc, Name, Marks;  
``
