-- A script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.
-- Can't use JOIN.
SELECT
	id,
	name
FROM
	cities
WHERE
	state_id = (
        	 SELECT
			id
        	 FROM
			states
        	 WHERE
			name = 'California'
    		 );
