CREATE TABLE events (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  start_date TIMESTAMP NOT NULL,
  end_date TIMESTAMP NOT NULL,
  location VARCHAR(255) NOT NULL,
  price REAL,
  tag VARCHAR(255) REFERENCES (tags.tag) -- this might not work; fix later
);

CREATE TABLE clubs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    tag VARCHAR(255) REFERENCES (tags.tag), -- this might not work; fix later
    closest_tag_1 VARCHAR(255),
    closest_tag_2 VARCHAR(255),
    closest_tag_3 VARCHAR(255) -- TRY BETTER WAY TO STORE LIST OF TAGS
)

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    tag VARCHAR(255) NOT NULL,
    closest_tag_1 VARCHAR(255),
    closest_tag_2 VARCHAR(255),
    closest_tag_3 VARCHAR(255) -- TRY BETTER WAY TO STORE LIST OF TAGS
)

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    misc_information VARCHAR(2047),
    preference_tag_1 VARCHAR(255),
    preference_tag_2 VARCHAR(255),
    preference_tag_3 VARCHAR(255) -- TRY BETTER WAY TO STORE LIST OF TAGS
)
