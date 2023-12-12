-- A script that lists all the records in the table `second_table` where
-- the record has a name.
SELECT
	score,
	`name`
FROM
	second_table
WHERE
	`name` is not NULL
ORDER BY
      score DESC
;
