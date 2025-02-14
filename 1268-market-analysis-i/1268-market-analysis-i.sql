with cte1 as (
    select buyer_id, count(1) as orders_in_2019
    from Orders
    where year(order_date)= 2019
    group by buyer_id
)
select Users.user_id as buyer_id, Users.join_date,
coalesce(orders_in_2019,0) as orders_in_2019
from Users
left join cte1
on Users.user_id = cte1.buyer_id;
