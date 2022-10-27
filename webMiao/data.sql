create database 2022XSCTF_webMiao;
use 2022XSCTF_webMiao;

create table if not exists images
(
	id int auto_increment
		primary key,
	path varchar(100) null
)
;

create table if not exists users
(
	username varchar(100) not null
		primary key,
	password varchar(100) null
)
;

INSERT INTO images (id, path) VALUES (1, 'images/maoyuna.jpg');
INSERT INTO images (id, path) VALUES (2, 'images/miaowu.jpg');
INSERT INTO images (id, path) VALUES (3, 'images/aowu.jpg');
INSERT INTO images (id, path) VALUES (4, 'images/miaonei.jpg');

INSERT INTO users values ('admin', SUBSTR(MD5(RAND()),1,20));