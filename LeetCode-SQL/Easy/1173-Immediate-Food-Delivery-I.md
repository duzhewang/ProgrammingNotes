Problem: 1173

MySQL: 

```
Select round(T.d/count(delivery_id)*100,2) as immediate_percentage from Delivery as D,  
(select count(delivery_id) as d from Delivery where order_date=customer_pref_delivery_date) as T;



```
