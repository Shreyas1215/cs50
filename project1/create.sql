create table books2 (
  id SERIAL PRIMARY KEY,
  isbn VARCHAR UNIQUE NOT NULL,
  title VARCHAR NOT NULL,
  author VARCHAR NOT NULL,
  year SMALLINT NOT NULL
);

create table users1 (
  id SERIAL PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL
);


CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users1,
    book_id INTEGER REFERENCES books2,
    rating SMALLINT NOT NULL CONSTRAINT Invalid_Rating CHECK (rating <=5 AND rating>=1),
    comment VARCHAR
);
