-- A script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.
-- Can't use JOIN.
SELECT
	id,
	name
FROM
	states AS s,
	citites AS c
WHERE
	s.id = c.id
	AND
	c.name = 'California'
ORDER BY
      c.id DESC
