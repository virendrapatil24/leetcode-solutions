# Write your MySQL query statement below
With temp as
(
Select *
from stadium
where people >= 100
)

Select distinct s.id, s.visit_date, s.people
from stadium s,
(
Select t1.id as startid, t1.id+2 as endid
from temp t1, temp t2, temp t3
where t1.id+1 = t2.id
and t2.id+1 = t3.id
) t
where s.id between t.startid and t.endid;