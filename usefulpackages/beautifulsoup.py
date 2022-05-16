import requests
from bs4 import BeautifulSoup

def get_movies_list():
    response = requests.get("https://www.imdb.com/list/ls055386972/", headers={"Accept-Language":"en-US"})
    soup = BeautifulSoup(response.content, "html.parser")

    movies = []
    for movie in soup.find_all("div", class_="lister-item-content"):
        title = movie.find("h3").find("a").string
        duration = int(movie.find("span", class_="runtime").string.strip(' min'))
        movies.append({'title': title, 'duration': duration})

    return movies
