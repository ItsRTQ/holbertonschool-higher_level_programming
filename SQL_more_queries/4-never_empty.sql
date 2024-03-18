-- This sql script creates a table and sets id to 1 as default
CREATE TABLE IF NOT EXISTS id_not_null ( id INT DEFAULT 1,
name VARCHAR(256)
);