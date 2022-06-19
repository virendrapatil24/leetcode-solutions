with temp as
(
    Select d.name as Dname, e.name as Ename, e.salary as Salary, 
    rank() over(partition by d.name order by salary desc) as rankk
    from employee e
    join department d
    on e.departmentId = d.id
)

select Dname as Department,
Ename as Employee,
Salary
from temp
where rankk = 1

