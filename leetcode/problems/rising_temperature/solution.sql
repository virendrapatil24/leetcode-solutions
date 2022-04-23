# Write your MySQL query statement below
select b.id 
from Weather a, Weather b 
where a.recordDate = (b.recordDate - interval 1 day)
and b.temperature > a.temperature