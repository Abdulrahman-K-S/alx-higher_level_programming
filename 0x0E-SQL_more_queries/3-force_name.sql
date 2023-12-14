-- A script that creates the table `force_name` on the given database.
-- The table has id -> int & name -> varchar(256)
CREATE TABLE if not exists force_name (
       id INT,
       `name` VARCHAR(256) NOT NULL
);
