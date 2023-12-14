-- A script that creats the database `hbtn_0d_usa` and creates the table `states` in it
-- Table description
-- 	 - id INT not null PK auto generated
-- 	 - name VARCHAR(256) not null
CREATE DATABASE if not exists hbtn_0d_usa;
CREATE TABLE if not exists hbtn_0d_usa.states(
       id INT PRIMARY KEY AUTO_INCREMENT,
       name VARCHAR(256) NOT NULL
);
