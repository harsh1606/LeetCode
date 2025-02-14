# Write your MySQL query statement below

-- select distinct C.name
-- from Orders as A
-- left join Company as B
-- on A.com_id = B.com_id
-- right join SalesPerson as C
-- on A.sales_id = C.sales_id
-- where B.name != 'RED';

select name
from SalesPerson
where sales_id not in (
    select A.sales_id
    from SalesPerson as A
    left join Orders as B
    on A.sales_id = B.sales_id
    left join Company as C
    on B.com_id = C.com_id
    where C.name = 'RED'
);