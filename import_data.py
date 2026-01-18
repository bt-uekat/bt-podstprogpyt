import csv
from database import engine, SessionLocal, Base, Movie, Link, Rating, Tag

Base.metadata.create_all(bind=engine)


def load_csv_data():
    db = SessionLocal()

    if db.query(Movie).count() == 0:
        print("Importowanie filmów...")
        with open('movies.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                movie = Movie(
                    movieId=int(row['movieId']),
                    title=row['title'],
                    genres=row['genres']
                )
                db.add(movie)
        db.commit()
        print("Filmy zaimportowane.")

    if db.query(Link).count() == 0:
        print("Importowanie linków...")
        with open('links.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                link = Link(
                    movieId=int(row['movieId']),
                    imdbId=row['imdbId'],
                    tmdbId=row['tmdbId']
                )
                db.add(link)
        db.commit()
        print("Linki zaimportowane.")

    if db.query(Tag).count() == 0:
        print("Importowanie tagów...")
        with open('tags.csv', encoding='utf-8') as f:
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
        print("Tagi zaimportowane.")

    if db.query(Rating).count() == 0:
        print("Importowanie ocen (to może chwilę potrwać)...")
        with open('ratings.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            batch = []
            for i, row in enumerate(reader):
                rating = Rating(
                    userId=int(row['userId']),
                    movieId=int(row['movieId']),
                    rating=float(row['rating']),
                    timestamp=int(row['timestamp'])
                )
                db.add(rating)
                if i > 1000:
                    break

        db.commit()
        print("Oceny zaimportowane.")

    db.close()


if __name__ == "__main__":
    load_csv_data()
