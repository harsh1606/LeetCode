# Write your MySQL query statement below
with grp as (
    select id, visit_date,people,
    id - row_number() over(order by id) as diff
    from Stadium
    where people >= 100
)
select id, visit_date, people
from grp
where diff in (
    select diff
    from grp
    group by diff
    having count(1) > 2
)