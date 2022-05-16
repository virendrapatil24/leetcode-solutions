# Write your MySQL query statement below
with temp as(
Select t.request_at, 
Case
    when t.status = 'cancelled_by_driver' or t.status = 'cancelled_by_client' then 1
    else 0
end as binary_status
from Trips t
join Users u on t.client_id = u.users_id 
join Users u1 on t.driver_id = u1.users_id
where u.banned != 'Yes' 
and u1.banned != 'Yes'
and t.request_at between "2013-10-01" and "2013-10-03"
)

select request_at as Day, 
round(sum(binary_status) / count(*),2) as 'Cancellation Rate'
from temp
group by request_at

