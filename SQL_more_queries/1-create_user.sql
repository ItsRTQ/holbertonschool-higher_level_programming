-- This script creates a user with set password
SELECT EXISTS (
    SELECT 1 
    FROM mysql.user 
    WHERE user = 'user_0d_1' AND host = '%'
) INTO @user_exists;

IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';
    FLUSH PRIVILEGES;
END IF;
