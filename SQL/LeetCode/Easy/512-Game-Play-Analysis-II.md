Problem: 512

SQL:

```
Select A.player_id, A.device_id from Activity as A Join 
(Select player_id, min(event_date) as first_login from Activity group by player_id) as T
on A.player_id=T.player_id and A.event_date=T.first_login; 
```
