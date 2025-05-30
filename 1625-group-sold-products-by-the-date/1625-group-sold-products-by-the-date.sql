# Write your MySQL query statement below

select sell_date,count(distinct product) as num_sold,
    GROUP_CONCAT(distinct product order by product SEPARATOR ',') as products                     
from Activities
group by 1
order by 1;