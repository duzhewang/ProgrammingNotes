Problem: Query the Name of any student in STUDENTS who scored higher than 75 Marks. 
Order your output by the last three characters of each name. 
If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.


SQL: ``Select Name from Students where Marks>75 order by Right(Name,3) asc,ID asc;``



Remark: ``Right(text, 3)`` choose the last three characters 
