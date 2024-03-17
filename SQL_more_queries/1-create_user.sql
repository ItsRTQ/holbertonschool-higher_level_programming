-- This script creates a user with set password
IF NOT EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost') THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
END IF;
