select 
(case 
    when mod(id, 2) != 0 and counts != id then id + 1 
    when mod(id, 2) != 0 and counts = id then id 
    when mod(id, 2) = 0 then id - 1
    END
) as id, student 
from seat, 
    (select count(*) as counts from seat) as seat_counts
order by id ASC;
