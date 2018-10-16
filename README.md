## Rzepa - example of simple REST API server.


_"The single hardest thing in programmer's work is naming things."_


This is a simple REST API server with 3 endpoints and some external API synchronization. It is build with Django and Django Rest Framework and run on Docker containers.


### Installation

* Install [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/)
* Clone the code
* In repository directory, prepare required paths and provide them with proper ownership:
    `mkdir dbdata static media && chown 999:999 dbdata/ static/ media/`
* create a `.env` file with required configuration as in example:

```DJANGO_SECRET_KEY=key
DJANGO_SETTINGS_MODULE=rzepa.settings
DJANGO_DATABASE_URL=postgres://user:pass@db:5432/db_name
POSTGRES_PASSWORD=pass
POSTGRES_USER=user
OMDB_API_KEY=omdb_api_key
OMDB_API_URL=http://www.omdbapi.com
```

* build and start the application:
    `sudo docker-compose build && docker-compose up`

* now, application is visible on http://127.0.0.1


### Development

* __Important__: in order to be able to create migrations docker user must be the owner of migration directory. It can be easily achieved with `chown 999:999 rzepa/movies/migrations/ rzepa/comments/migrations`


### Testing

* In order to run tests run (after successful installation, of course):
    `docker-compose run web pytest .`


### API reference:

`GET /movies` - returns list of all movies.

`GET /movies {"title": "that movie"}` - returns list of movies matching given title

`POST /movies {"title": "Shawshank"}` - searches OMDb API for movie "Shawshank", saves the best matching one onto the database and returns fetched data. If This movie is already saved in the database returns the existing data. If `title` is not provided raises a 400

`GET /comments` - returns all comments from the database

`GET /comments {"movie_pk": 123}` - returns all comments for movie with id `123`

`POST /comments {"movie": 123, "text": "comment text", "author": "author name"}` - posts a comment to movie with id `123` with text "comment text" authored by "author name". If author is not provided, it will be saved as "Anonymous".

`GET /top {"from": <date>, "to": <date>}` - returns list of movies with top comments. If `from` and/or `to` are provided, only comments created in given time range will be returned (therefore for example movies with no comments will be not present with those parameters on).
