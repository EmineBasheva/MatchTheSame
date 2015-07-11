DROP TABLE IF EXISTS Classification;

CREATE TABLE Classification(
    id INTEGER PRIMARY KEY,
    name TEXT,
    points INTEGER,
    board_width INTEGER,
    board_height INTEGER
);