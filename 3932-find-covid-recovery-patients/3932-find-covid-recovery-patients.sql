with cte1 as (
    select patient_id, min(test_date) as first_pos_dt
    from covid_tests 
    where result = 'Positive'
    group by patient_id
),
cte2 as (
    select ct.patient_id, min(test_date) as first_neg_dt
    from covid_tests as ct
    inner join cte1
    on ct.patient_id = cte1.patient_id
    where ct.result = 'Negative'
    and ct.test_date >= cte1.first_pos_dt
    group by ct.patient_id 
)
select cte1.patient_id, P.patient_name, P.age, 
datediff(cte2.first_neg_dt, cte1.first_pos_dt) as recovery_time 
from cte1
inner join cte2
on cte1.patient_id = cte2.patient_id
left join patients as P
on cte1.patient_id = P.patient_id
order by recovery_time, P.patient_name;