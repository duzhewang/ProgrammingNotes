Problem: 1070

SQL:

```
Select T.product_id, T.first_year, S.quantity, S.price from Sales as S Join 
(Select product_id, min(year) as first_year from Sales group by product_id) as T
on T.product_id=S.product_id and T.first_year=S.year; 
```
