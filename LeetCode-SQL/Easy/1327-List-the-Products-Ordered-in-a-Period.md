Problem: 1327

SQL: 

```
Select product_name, unit from 
(Select P.product_name as Product_name, sum(O.unit) as unit from Products as P Join Orders as O on P.product_id=O.product_id where O.order_date between '2020-02-01' and '2020-02-29' group by P.product_name) as T
where unit>=100;

```
