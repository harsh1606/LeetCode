# Write your MySQL query statement below

with cte1 as  (
    select employee_id,rating,review_id , review_date,
    lag(rating,1) over(partition by employee_id order by review_date) as last_rating,
    lag(rating,2) over(partition by employee_id order by review_date) as sec_last_rating,
    row_number() over(partition by employee_id order by review_date desc) as dt_ranking,
    rating - lag(rating,2) over(partition by employee_id order by review_date) as improvement_score 
    from performance_reviews
)
select cte1.employee_id, name,
improvement_score
from cte1 
left join employees 
on cte1.employee_id = employees.employee_id 
where improvement_score  > 0 and improvement_score  is not null
and last_rating < rating
and sec_last_rating < last_rating 
and dt_ranking = 1
order by improvement_score desc, employees.name;
