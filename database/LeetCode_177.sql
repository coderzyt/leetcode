CREATE FUNCTION getNthHighestSalary(N int) RETURNS int
BEGIN
    set n = N - 1;
    RETURN (
        select IFNULL((select DISTINCT Salary as getNthHighestSalary from Employee order by Salary DESC limit 1 offset n), NULL)
    );
END