# Write your MySQL query statement below

with cte1 as (
    (
        select requester_id as id
        from RequestAccepted
    )
    union all 
    (
        select accepter_ID as id
        from RequestAccepted
    )
)
select id, count(1) as num
from cte1 
group by id
order by count(1) desc
limit 1;
