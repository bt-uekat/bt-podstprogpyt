from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
import models

app = FastAPI()


@app.get("/")
def read_root():
    return {'hello': 'world'}


@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    return db.query(models.Movie).limit(60).all()


@app.get("/links")
def get_links(db: Session = Depends(get_db)):
    return db.query(models.Link).all()


@app.get("/ratings")
def get_ratings(db: Session = Depends(get_db)):
    return db.query(models.Rating).limit(100).all()


@app.get("/tags")
def get_tags(db: Session = Depends(get_db)):
    return db.query(models.Tag).all()
