# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below

delete j 
from Person i, Person j
where i.email = j.email
and i.id < j.id