-- lists all privileges of the MySQL users user_0d_1 and user_0d_2
GRANT ALL PRIVILEGES ON *.* TO `user_0d_1`@`localhost`;
ALTER USER `user_0d_1`@`localhost` IDENTIFIED  BY'user_0d_1_pwd';
FLUSH PRIVILEGES;
