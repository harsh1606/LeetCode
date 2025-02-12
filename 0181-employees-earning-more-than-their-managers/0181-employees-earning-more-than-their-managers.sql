# Write your MySQL query statement below

select A.name as Employee
from Employee as A
inner join Employee as B
on A.managerId = B.id
where A.salary > B.salary;