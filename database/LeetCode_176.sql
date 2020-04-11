select DISTINCT Salary as SecondHighestSalary from Employee order by Salary DESC limit 1 offset 1;

select (select DISTINCT Salary from Employee order by Salary DESC limit 1 offset 1) as SecondHighestSalary;

select IFNULL((select DISTINCT Salary from Employee order by Salary DESC limit 1 offset 1), NULL) as SecondHighestSalary;