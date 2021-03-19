select all_trips.Request_at as Day, round(
    sum(case when Status = "cancelled_by_driver" or Status = "cancelled_by_client" then 1 else 0 end) / count(1), 2) as `Cancellation Rate`
from (select * from Users where Role = 'client' and Banned = 'No') not_banned_users
join
(select * from Trips where Request_at between "2013-10-01" and "2013-10-03") all_trips on all_trips.Client_Id = not_banned_users.Users_Id
group by all_trips.Request_at
order by all_trips.Request_at ASC;