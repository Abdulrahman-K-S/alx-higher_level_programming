-- A script that lists all the record of the table `second_table`
-- with `score >= 10` from the database `hbtn_0c_0`. Ordered by score
SELECT score, `name` FROM second_table WHERE score >= 10 ORDER BY score DESC;
