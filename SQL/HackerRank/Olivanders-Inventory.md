Problem: https://www.hackerrank.com/challenges/harry-potter-and-wands/problem

SQL:
```
SELECT id, age, m.coins_needed, m.power FROM 
(SELECT code, power, MIN(coins_needed) AS coins_needed FROM Wands GROUP BY code, power) AS m
JOIN Wands AS w ON m.code = w.code AND m.power = w.power AND m.coins_needed = w.coins_needed
JOIN Wands_Property AS p ON m.code = p.code
WHERE p.is_evil = 0
ORDER BY m.power DESC, age DESC;
```

MySQL:
```

Select W3.id, T.age, T.coins_needed, T.power from Wands as W3
join
(Select W1.code, W2.age, min(W1.coins_needed) as coins_needed, W1.power from Wands as W1
join Wands_Property as W2
on W1.code=W2.code
where W2.is_evil=0  
group by W1.code, W2.age, W1.power) as T
on W3.code=T.code and W3.coins_needed=T.coins_needed and W3.power=T.power
order by T.power desc, T.age desc; 



```
