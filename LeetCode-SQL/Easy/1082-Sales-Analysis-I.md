Problem: 1082

SQL:

```
Select seller_id from Sales group by seller_id having sum(price)=
(Select top 1 sum(price) as price from Sales group by seller_id order by price desc)

```
