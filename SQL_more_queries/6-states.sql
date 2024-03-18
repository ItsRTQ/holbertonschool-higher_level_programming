-- This script creates a database and table
CREATE database IF NOT EXISTS hbtn_0d_usa
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(PRIMARY KEY (id),
id INT NOT NULL KEY AUTO_INCREMENT,
name VARCHAR(256) NOT NULL);