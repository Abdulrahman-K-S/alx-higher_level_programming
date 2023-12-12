-- A script that lists the number of scores with the same values in
-- table `second_table`.
SELECT
	score,
	count(score) as number
FROM
	second_table
GROUP BY
      score
ORDER BY
      score DESC
;
