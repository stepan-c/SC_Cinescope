#constants
BASE_URL = "https://auth.dev-cinescope.coconutqa.ru"
CREATE_URL = "https://api.dev-cinescope.coconutqa.ru"
REGISTER_ENDPOINT = "/register"
LOGIN_ENDPOINT = "/login"
MOVIES_ENDPOINT = "/movies"

ADMIN_DATA = {
    "email": "api1@gmail.com",
    "password": "asdqwe123Q"
}


def film_data():
    return {
        "name": "qwe",
        "imageUrl": "https://example.com/image.png",
        "price": 300,
        "description": "Фальшивый фильм",
        "location": "SPB",
        "published": True,
        "genreId": 1
    }

def movies_data():
    return {
        "pageSize": 10,
        "page": 1,
        "minPrice": 1,
        "maxPrice": 1000,
        "locations": "SPB",
        "published": True,
        "genreId": None,
        "createdAt": "asc",

    }

def fake_movies_data():
    return {
        "pageSize": 10,
        "page": 1,
        "minPrice": 1,
        "maxPrice": 1000,
        "locations": "GZN",
        "published": True,
        "genreId": None,
        "createdAt": "asc",

    }

