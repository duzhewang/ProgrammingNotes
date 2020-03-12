Problem: https://www.hackerrank.com/challenges/weather-observation-station-19/problem?h_r=next-challenge&h_v=zen

MySQL: 
``select Round(sqrt(pow(max(LAT_N)-min(LAT_N),2)+power(max(LONG_W)-min(LONG_W), 2)),4) from Station;`` 
