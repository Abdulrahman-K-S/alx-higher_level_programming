-- A script that creats the user `user_0d_1`
CREATE USER if not exists 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'USER_0D_1'@'localhost';
FLUSH PRIVILEGES;
