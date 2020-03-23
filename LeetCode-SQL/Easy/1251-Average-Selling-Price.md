Problem: 1251

MySQL: 

```
select P.product_id, round(sum(P.price*U.units)/sum(U.units), 2) as average_price from Prices as P Join UnitsSold as U 
on P.product_id=U.product_id and 
U.purchase_date between P.start_date and P.end_date
group by P.product_id; 

```
