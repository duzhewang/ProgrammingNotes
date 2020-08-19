Problem: https://www.hackerrank.com/challenges/draw-the-triangle-2/problem

MySQL: 
``
Set @number=0; 
Select repeat('* ', @number:=@number+1) from information_schema.tables limit 20; 
``
