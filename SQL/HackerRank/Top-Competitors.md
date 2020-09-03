Problem: https://www.hackerrank.com/challenges/full-score/problem

SQL: 
```
SELECT h.hacker_id, h.name FROM Submissions AS s JOIN Hackers AS h ON s.hacker_id = h.hacker_id
JOIN Challenges AS c ON s.challenge_id = c.challenge_id
JOIN Difficulty AS d ON c.difficulty_level = d.difficulty_level
where s.score=d.score group by h.hacker_id, h.name having count(*)>1 order by count(*) desc, h.hacker_id;
```
