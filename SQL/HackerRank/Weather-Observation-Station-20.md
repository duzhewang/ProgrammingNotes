Problem: https://www.hackerrank.com/challenges/weather-observation-station-20/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

MySQL: 
```
Set @rowIndex=-1; 
Select Round(Avg(t.LAT_N),4) from 
(
SELECT @rowIndex := @rowIndex+1 AS rowIndex, s.LAT_N FROM STATION AS s ORDER BY s.LAT_N asc
) As t where t.rowIndex in (floor(@rowindex/2), ceil(@rowindex/2))
```

```
Set @rowindex=0; 
Select  round(AVG(LAT_N), 4) from 
(Select LAT_N, @rowindex:=@rowindex+1 as rowindex from Station
order by LAT_N asc) as temp
where temp.rowindex in (floor((@rowindex+1)/2), ceil((@rowindex+1)/2));
```
