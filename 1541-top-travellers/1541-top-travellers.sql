# Write your MySQL query statement below

-- select name, travelled_distance
-- from (
select U.name as name, sum(coalesce(distance,0)) as travelled_distance 
from Users as U
left join Rides as R
on U.id = R.user_id
group by U.id,1
order by 2 desc,1
-- ) as sv;


