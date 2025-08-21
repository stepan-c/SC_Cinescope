#data_generator
from faker import Faker

class DataGenerator:
    faker = Faker("ru_RU")

    @staticmethod
    def generator_email():
        return DataGenerator.faker.unique.email()


    @staticmethod
    def name_generator():
        return DataGenerator.faker.name()

    @staticmethod
    def generate_user_data():
        return {
            "email": DataGenerator.generator_email(),
            "fullName": DataGenerator.name_generator(),
            "password": "12345678Aa",
            "passwordRepeat": "12345678Aa"
        }

    @staticmethod
    def film_generator():
        return "St" + DataGenerator.faker.unique.name()

    @staticmethod
    def generator_film_data():
        return {
            "name": DataGenerator.film_generator(),
            "imageUrl": "https://example.com/image.png",
            "price": 300,
            "description": "Фальшивый фильм",
            "location": "SPB",
            "published": True,
            "genreId": 1
        }

    @staticmethod
    def patch_movie_data():
        return {
            "name": "Stepan" + DataGenerator.name_generator(),
            "imageUrl": "https://example.com/image.png",
            "price": 1000,
            "description": "Настоящий фильм",
            "location": "SPB",
            "published": True,
            "genreId": 1
        }

    @staticmethod
    def generator_fake_film_data():
        return {
            "name": DataGenerator.film_generator(),
            "imageUrl": "https://example.com/image.png",
            "price": 300,
            "description": "Фальшивый фильм",
            "location": "GBZ",
            "published": True,
            "genreId": 1
        }

    @staticmethod
    def patch_fake_movie_data():
        return {
            "name": "Stepan" + DataGenerator.name_generator(),
            "imageUrl": "https://example.com/image.png",
            "price": 1000,
            "description": "Настоящий фильм",
            "location": "GBZ",
            "published": True,
            "genreId": 1
        }