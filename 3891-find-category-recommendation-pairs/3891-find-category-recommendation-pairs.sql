with cte1 as (
    select user_id, category,
    sum(ifnull(quantity ,0)) as tot_qua
    from ProductPurchases as P
    left join ProductInfo as Pinfo
    on P.product_id = Pinfo.product_id 
    group by user_id, category
)
select category1, category2, sum(cnt) as customer_count 
from (
    select A.user_id, least(A.category, B.category) as category1   ,
    greatest(A.category,B.category) as category2,
    1 as cnt
    from cte1 as A
    join cte1 as B
    on A.user_id = B.user_id
    where A.category != B.category 
    group by A.user_id, least(A.category, B.category), greatest(A.category,B.category)
) as abc
group by category1, category2
having customer_count > 2
order by customer_count desc, category1 , category2;