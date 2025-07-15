select user_id , 
round(avg(case when activity_type = 'free_trial' then activity_duration end), 2) as trial_avg_duration,
round(avg(case when activity_type = 'paid' then activity_duration end), 2) as paid_avg_duration  
from UserActivity 
-- where user_id in (select distinct user_id
--                     from UserActivity
--                     where activity_type = 'paid')
group by user_id 
having Avg(CASE WHEN activity_type = 'paid' THEN activity_duration END) IS NOT NULL
