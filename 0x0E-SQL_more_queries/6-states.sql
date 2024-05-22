-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE hbtn_0d_usa;
CREATE TABLE hbtn_0d_usa(
id INT UNIQUE NOT NULL AUTO_INCREMENT,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id)
);
