select employee_id
from (
    select A.employee_id, A.name, B.salary
    from Employees as A
    left join Salaries as B
    on A.employee_id = B.employee_id
    union 
    select B.employee_id, A.name, B.salary
    from Employees as A
    right join Salaries as B
    on A.employee_id = B.employee_id
) as abc
where name is null or salary is null
order by employee_id;