DROP TABLE IF EXIST board;

CREATE TABLE board (
    id integer PRIMARY KEY AUTOINCREMENT, 
    title varchar(50), 
    message varchar(200)
    );

INSERT INTO board(title, message) VALUES ('title1', 'message1');
INSERT INTO board(title, message) VALUES ('title2', 'message2');