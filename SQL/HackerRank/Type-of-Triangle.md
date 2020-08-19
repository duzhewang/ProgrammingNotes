Problem: Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. 

Output one of the following statements for each record in the table:

Equilateral: It's a triangle with 3 sides of equal length.
Isosceles: It's a triangle with 2 sides of equal length.
Scalene: It's a triangle with 1 sides of differing lengths.
Not A Triangle: The given values of A, B, and C don't form a triangle.


SQL:  ``SELECT Case When not (A+B>C and A+C>B and B+C>A) Then "Not A Triangle"
When A=B and B=C  Then "Equilateral"
When A=B or B=C or A=C Then "Isosceles"
Else "Scalene"
end 
from Triangles``
