-- This sql script creates a table and sets id to 1 as default
CREATE TABLE IF NOT EXISTS unique_id ( id INT default 1,
name VARCHAR(256),
CONSTRAINT unique_id_default_unique UNIQUE (id)
);