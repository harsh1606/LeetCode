with cte1 as (
    select driver_id ,
    avg(distance_km / fuel_consumed) as first_half_avg   
    from trips
    where month(trip_date) in (1,2,3,4,5,6)
    group by driver_id
),
cte2 as (
    select driver_id ,
    avg(distance_km / fuel_consumed) as second_half_avg      
    from trips
    where month(trip_date) not in (1,2,3,4,5,6)
    group by driver_id 
)
select cte1.driver_id, driver_name, 
round(first_half_avg,2) as first_half_avg, 
round(second_half_avg, 2) as second_half_avg,
round((second_half_avg - first_half_avg), 2) as efficiency_improvement 
from cte1 
inner join cte2
on cte1.driver_id = cte2.driver_id
left join drivers
on drivers.driver_id = cte1.driver_id 
where second_half_avg > first_half_avg
order by efficiency_improvement desc, driver_name;
