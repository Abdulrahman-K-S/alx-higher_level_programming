-- A script that creates the database `hbtn_0d_2`
-- and the user `user_0d_2` with SELECT privileges only
CREATE DATABASE if not exists hbtn_0d_2;
CREATE USER if not exists 'user_0d_2'@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT on hbtn_0d_2.* TO 'user_0d_2'@localhost;
FLUSH PRIVILEGES;
