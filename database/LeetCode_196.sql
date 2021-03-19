delete from Person where Id not in (select p.id from (select min(Id) as id from Person group by Email) as p);
