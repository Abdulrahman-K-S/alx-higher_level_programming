-- A script that creates the table `first_table` in the inputed database
-- if the table already exists the script shouldn't fail.
CREATE TABLE if not exists first_table (
       id INT,
       name VARCHAR(256)
);
