-- A script that creates the table `cities` in the db `hbtn_0d_usa`.
-- Table descriptions:
-- 	 - id INT PK AUTO_INCREMENT
--	 - state_id INT FK NOT NULL
-- 	 - name VARCHAR(256) NOT NULL
CREATE DATABASE if not exists hbtn_0d_usa;
CREATE TABLE if not exists hbtn_0d_usa.cities (
       id INT PRIMARY KEY AUTO_INCREMENT,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       FOREIGN KEY (state_id) REFERENCES states(id)
);
