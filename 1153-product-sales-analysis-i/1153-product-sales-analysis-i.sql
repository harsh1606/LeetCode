# Write your MySQL query statement below
select product_name, year, price
from Sales as A
left join Product as B
on A.product_id = B.product_id;