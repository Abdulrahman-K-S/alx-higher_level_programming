-- A script that creats a new table `second_table` in the database `hbtn_0c_0`
-- and inserts in some values (adds multiple rows).
CREATE TABLE if not exists second_table (
       id INT,
       `name` VARCHAR(256),
       score INT
);

INSERT INTO second_table (id, `name`, score) values
       (1, 'John', 10),
       (2, 'Alex' ,3),
       (3, 'Bob', 14),
       (4, 'George', 8)
;
