import csv
from typing import List, Optional
from fastapi import FastAPI

app = FastAPI()


class Movie:
    def __init__(self, id, title, genres):
        self.id = id
        self.title = title
        self.genres = genres


class Link:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp


# zadanie 1
@app.get("/")
def read_root():
    return {'hello': 'world'}


# zadanie 2
@app.get("/movies")
def get_movies():
    movies_list = []
    try:
        with open('movies.csv', mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                movie = Movie(
                    id=row['movieId'],
                    title=row['title'],
                    genres=row['genres']
                )
                movies_list.append(movie)
    except FileNotFoundError:
        return {"error": "Plik movies.csv nie został znaleziony."}

    return [movie.__dict__ for movie in movies_list[:60]]


# zadanie 4

@app.get("/links")
def get_links():
    links_list = []
    try:
        with open('links.csv', mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                link = Link(row['movieId'], row['imdbId'], row['tmdbId'])
                links_list.append(link)
    except FileNotFoundError:
        return {"error": "Plik links.csv nie został znaleziony."}
    return [link.__dict__ for link in links_list]


@app.get("/ratings")
def get_ratings():
    ratings_list = []
    try:
        with open('ratings.csv', mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                if i >= 100:
                    break
                rating = Rating(
                    row['userId'], row['movieId'],
                    row['rating'], row['timestamp']
                )
                ratings_list.append(rating)
    except FileNotFoundError:
        return {"error": "Plik ratings.csv nie został znaleziony."}
    return [rating.__dict__ for rating in ratings_list]


@app.get("/tags")
def get_tags():
    tags_list = []
    try:
        with open('tags.csv', mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tag = Tag(
                    row['userId'], row['movieId'],
                    row['tag'], row['timestamp']
                )
                tags_list.append(tag)
    except FileNotFoundError:
        return {"error": "Plik tags.csv nie został znaleziony."}
    return [tag.__dict__ for tag in tags_list]
