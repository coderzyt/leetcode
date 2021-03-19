select w1.Id from Weather w1 join Weather w2 on DATEDIFF(w1.RecordDate, w2.RecordDate) = 1 and w1.Temperature > w2.Temperature;

select w1.Id from Weather w1 join Weather w2 on TIMESTAMPDIFF(day, w1.RecordDate, w2.RecordDate) = 1 and w1.Temperature > w2.Temperature;