Problem: https://www.hackerrank.com/challenges/contest-leaderboard/problem?h_r=next-challenge&h_v=zen

SQL: 
``
Select T1.hacker_id, T1.name, sum(T1.score) from
(Select S.hacker_id as hacker_id, H.name as name, max(S.score) as score from Submissions as S Join Hackers as H ON S.hacker_id=H.hacker_id group by S.hacker_id, H.name, S.challenge_id) as T1 
group by T1.hacker_id, T1.name having sum(T1.score)>0
order by sum(T1.score) desc, T1.hacker_id asc; 
``
