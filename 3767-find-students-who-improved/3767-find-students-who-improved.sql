with cte1 as (
    select student_id,subject, score, exam_date,
    row_number() over(partition by student_id, subject order by exam_date) as first_exam_dt,
    row_number() over(partition by student_id, subject order by exam_date desc) as last_exam_dt
    from Scores
),
cte2 as (
    select student_id, subject, score as first_score
    from cte1
    where first_exam_dt = 1
),
cte3 as (
    select student_id, subject, score as latest_score
    from cte1
    where last_exam_dt = 1
)
select cte2.student_id, cte2.subject,
first_score, latest_score
from cte2
inner join cte3
on cte2.student_id = cte3.student_id 
and cte2.subject = cte3.subject
where latest_score > first_score 
