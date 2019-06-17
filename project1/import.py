import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://hcedhaxdxjbfgh:cac63c37f5145faafe05528a76f465427230cf9c66765d71afa5f5630bfc0f83@ec2-174-129-240-67.compute-1.amazonaws.com:5432/d8gpqbigtp2jnt')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv", "r")  # needs to be opened during reading csv
    reader = csv.reader(f)
    next(reader)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books2 (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
               {"isbn": isbn, "title": title, "author": author, "year": year})
        db.commit()
        print(f"Added book with ISBN: {isbn} Title: {title}  Author: {author}  Year: {year}")


if __name__ == '__main__':
    main()
