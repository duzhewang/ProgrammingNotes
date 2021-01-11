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

Note: it doesn't matter if we use ```max``` or ```min``` 


2. [The Blunder](https://www.hackerrank.com/challenges/the-blunder/problem)

- Problem

```
Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's  key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeroes removed), and the actual average salary.

Write a query calculating the amount of error (i.e.:  average monthly salaries), and round it up to the next integer.


```

- Solution: use ```ceil``` and ```replace```

```

Select ceil(avg(salary)-avg(replace(salary, '0', ''))) from Employees 
```



3. [Weather observation station 20](https://www.hackerrank.com/challenges/weather-observation-station-20/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen)

- Problem: 
```
A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to  decimal places.
```

- Solution:
```
Set @rowindex=-1;
Select round(avg(LAT_N), 4) FROM 
(Select @rowindex:=@rowindex+1 as rownumber, LAT_N from Station
order by LAT_N ASC) AS t
where rownumber in (floor(@rowindex/2), ceil(@rowindex/2))




```


4. [Top competitors](https://www.hackerrank.com/challenges/full-score/problem)

```
SELECT h.hacker_id, h.name FROM Submissions AS s 
JOIN Hackers AS h 
ON s.hacker_id = h.hacker_id
JOIN Challenges AS c 
ON s.challenge_id = c.challenge_id
JOIN Difficulty AS d 
ON c.difficulty_level = d.difficulty_level
where s.score=d.score 
group by h.hacker_id, h.name 
having count(*)>1 
order by count(*) desc, h.hacker_id;




```


5. [Challenges](https://www.hackerrank.com/challenges/challenges/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=)

```
Select H.hacker_id, H.name, count(C.challenge_id) as num_challenge from Hackers as H
join Challenges as C
on H.hacker_id=C.hacker_id
group by H.hacker_id, H.name
having num_challenge=(select count(challenge_id) from Challenges group by hacker_id order by count(challenge_id) desc limit 1)
or num_challenge in 
(Select cnt from 
(select count(challenge_id) as cnt from Challenges group by hacker_id) as T
 group by cnt
having count(*)=1)
order by num_challenge desc, hacker_id; 


```











