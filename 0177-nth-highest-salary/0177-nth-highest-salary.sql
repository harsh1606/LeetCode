CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    select ifnull((
        select distinct salary
        from ( 
            select salary, 
            dense_rank() over(order by salary desc) as _rank
            from Employee
        ) abc
        where _rank = N
    ),Null)  
  );
END