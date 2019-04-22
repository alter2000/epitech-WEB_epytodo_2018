CREATE DATABASE IF NOT EXISTS epytodo;
USE epytodo;

DROP TABLE IF EXISTS user;
CREATE TABLE user
(
	user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(255) NOT NULL,
	password VARCHAR(255) NOT NULL,
	u_mail VARCHAR(255),
	u_tasks INT,
	u_tasks_completed INT
	UNIQUE_KEY(user_id, username)
) DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS task;
CREATE TABLE task
(
	task_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	begin TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	end TIMESTAMP DEFAULT 0,
	status INT DEFAULT 0,
	t_description VARCHAR(2048)
);

DROP TABLE IF EXISTS user_has_task;
CREATE TABLE user_has_task
(
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	fk_user_id INT NOT NULL FOREIGN KEY user_has_task(fk_user_id) REFERENCES task(task_id),
	fk_task_id INT NOT NULL FOREIGN KEY user_has_task(fk_task_id) REFERENCES user(user_id)
);
