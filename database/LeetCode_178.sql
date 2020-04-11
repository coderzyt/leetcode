-- select Score, dense_rank() over (order by Score DESC) as Rank from Scores;

select Score, dense_rank() over (order by Score DESC) as Rank from Scores;