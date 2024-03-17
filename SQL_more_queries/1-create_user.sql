-- This script creates a user with set password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED By 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
