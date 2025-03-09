# Write your MySQL query statement below

select name, travelled_distance
from (
    select U.id as id,U.name as name, sum(coalesce(distance,0)) as travelled_distance 
    from Users as U
    left join Rides as R
    on U.id = R.user_id
    group by 1,2
    order by 3 desc,2
) as sv;


