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


def filter_data():
    return [
        ("pageSize", 10),
        ("page", 1),
        ("minPrice", 1),
        ("maxPrice", 1000),
        ("locations", "SPB"),
        ("published", "true"),
        ("createdAt", "asc")
    ]

def fake_filter_data():
    return [
        ("pageSize", 10),
        ("page", 1),
        ("minPrice", 1),
        ("maxPrice", 1000),
        ("locations", "GZP"),
        ("published", "true"),
        ("createdAt", "asc")
    ]

class SuperAdminCreds:
    USERNAME = 'api1@gmail.com'
    PASSWORD = 'asdqwe123Q'