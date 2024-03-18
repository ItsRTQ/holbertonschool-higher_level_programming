-- This sql script creates a table and sets name to empty as default
CREATE TABLE IF NOT EXISTS force_name ( id INT,
name VARCHAR(256) DEFAULT ""
);