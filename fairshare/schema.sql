DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS flatshare;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  FOREIGN KEY (id) REFERENCES person (id)
);

CREATE TABLE person (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE flatshare (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  personIds INTEGER[] NOT NULL
);