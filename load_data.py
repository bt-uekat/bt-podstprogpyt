import csv
from database import SessionLocal, engine, Base

from models import Movie, Link, Rating, Tag

Base.metadata.create_all(bind=engine)


def load_csv_data():
    db = SessionLocal()

    print("Ładowanie filmów...")
    with open('movies.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            movie = Movie(
                id=int(row['movieId']),
                title=row['title'],
                genres=row['genres']
            )
            db.add(movie)

    print("Ładowanie linków...")
    with open('links.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            link = Link(
                movieId=int(row['movieId']),
                imdbId=row['imdbId'],
                tmdbId=row['tmdbId']
            )
            db.add(link)

    print("Ładowanie ocen (może chwilę potrwać)...")
    with open('ratings.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for i, row in enumerate(reader):
            rating = Rating(
                userId=int(row['userId']),
                movieId=int(row['movieId']),
                rating=float(row['rating']),
                timestamp=int(row['timestamp'])
            )
            db.add(rating)
            if i > 10000:
                break

    print("Ładowanie tagów...")
    with open('tags.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tag = Tag(
                userId=int(row['userId']),
                movieId=int(row['movieId']),
                tag=row['tag'],
                timestamp=int(row['timestamp'])
            )
            db.add(tag)

    db.commit()
    db.close()
    print("Zakończono ładowanie danych.")


if __name__ == "__main__":
    load_csv_data()
