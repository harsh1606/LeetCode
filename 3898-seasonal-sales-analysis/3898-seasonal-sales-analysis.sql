with cte1 as (
    select 
    (case 
        when month(A.sale_date) in (12,1,2) then 'Winter'
        when month(A.sale_date) in (3,4,5) then 'Spring' 
        when month(A.sale_date) in (6,7,8) then 'Summer'
        else 'Fall'
    end) as season,category,
    sum(quantity) as total_quantity ,
    sum(quantity * price) as total_revenue 
    from sales as A
    left join products as B
    on A.product_id = B.product_id
    group by 1, 2
)
select season, category, total_quantity, total_revenue
from (
    select season, category, total_quantity, total_revenue,
    row_number() over(partition by season order by total_quantity desc,total_revenue desc) as _rank
    from cte1
) as abc
where _rank = 1;
