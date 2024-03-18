-- This script creates database and tables
CREATE IF NOT EXISTS hbtn_0d_usa;
CREATE IF NOT EXISTS cities.hbtn_0d_usa (PRIMARY KEY (id),
id INT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id));