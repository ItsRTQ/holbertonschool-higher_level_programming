-- This script creates a database and table
CREATE database IF NOT EXISTS hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states(id INT KEY AUTO_INCREMENT,
CONSTRAINT unique_id_default_unique UNIQUE (id),
name VARCHAR(256) DEFAULT "");