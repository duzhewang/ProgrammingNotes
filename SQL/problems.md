# A collection of hard problems 

## Changing table formats

1. [Occupations](https://www.hackerrank.com/challenges/occupations/problem)

- Problem: 

```
Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. 
The output column headers should be Doctor, Professor, Singer, and Actor, respectively.
Note: Print NULL when there are no more names corresponding to an occupation.
```


- Solution: 

```
set @a=0, @b=0, @c=0, @d=0;
select max(D), max(P), max(S), max(A) from 
(select name, occupation, 
case when Occupation='Doctor'    then (@a:=@a+1)
            when Occupation='Professor' then (@b:=@b+1)
            when Occupation='Singer'    then (@c:=@c+1)
            when Occupation='Actor'     then (@d:=@d+1)     
        end as rownumber,
        if(Occupation='Doctor', name, null) as D,
        if(Occupation='Professor', name, null) as P,
        if(Occupation='Singer', name, null) as S,
        if(Occupation='Actor', name, null) as A
from OCCUPATIONS
order by name) as T
group by rownumber

```


