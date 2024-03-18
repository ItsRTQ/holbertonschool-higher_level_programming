-- This script creates database and tables
CREATE IF NOT EXISTS hbtn_0d_usa;
CREATE IF NOT EXISTS cities (PRIMARY KEY (id),
id INT NOT NULL,
state_id INT NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id),
name VARCHAR(256) NOT NULL);