import requests

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

for movie_id in movie_ids:
    url = f"https://nomad-movies.nomadcoders.workers.dev/movies/{movie_id}"
    response = requests.get(url)
    movie = response.json()
    print(movie["title"])
    print(movie["overview"])
    print(movie["vote_average"])
