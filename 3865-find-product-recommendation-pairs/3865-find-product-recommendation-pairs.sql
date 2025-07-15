with cte1 as (
    select A.product_id as product1_id , B.product_id as product2_id ,
    count(1) as customer_count 
    from ProductPurchases as A
    join ProductPurchases as B
    on A.user_id = B.user_id
    where A.product_id < B.product_id
    group by A.product_id, B.product_id
    having count(1) > 2
)
select cte1.product1_id  , cte1.product2_id  ,prod_info.category as product1_category ,
prod_info_2.category as product2_category, customer_count
from cte1 
left join ProductInfo as prod_info
on cte1.product1_id = prod_info.product_id
left join ProductInfo as prod_info_2
on cte1.product2_id = prod_info_2.product_id
order by cte1.customer_count desc, cte1.product1_id  , cte1.product2_id