-- A script that creates the table `unique_id` on the given database.
-- Table description:
-- 	 - id INT default 1 unique
-- 	 - name VARCHAR(256)
CREATE TABLE if not exists unique_id(
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256) NOT NULL
);
