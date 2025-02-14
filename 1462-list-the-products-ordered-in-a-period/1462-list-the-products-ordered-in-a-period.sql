# Write your MySQL query statement below

select B.product_name, sum(unit) as unit
from Orders as A
left join Products as B
on A.product_id = B.product_id
where year(order_date)*100 + month(order_date) = 202002
group by A.product_id
having sum(unit) >= 100;