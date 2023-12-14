-- A script that creates the table 'id_not_null' on the given database
-- Table description:
--	- id INT default 1
--	- name VARCHAR(256)
CREATE TABLE if not exists id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256)
);
