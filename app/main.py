from datetime import date
from fastapi import FastAPI, Query
from typing import Optional, Union

app = FastAPI()

@app.get('/hotels')
def get_hotels(
    location:str,
    date_from: date,
    date_to: date,
    has_spa: bool = None,
    stars: int = Query(None, ge=1, le=5),
):
  return location, date_from, date_to, has_spa, stars,
