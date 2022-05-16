# Write your MySQL query statement below

with temp as (
    Select dept.name as Department,
    emp.name as Employee,
    emp.salary as Salary,
    dense_rank() over (partition by dept.id order by emp.salary desc) as Rank_of_salary
    from employee emp
    join department dept
    on emp.departmentId = dept.id
)


Select Department, Employee, Salary
from temp
where Rank_of_salary <= 3