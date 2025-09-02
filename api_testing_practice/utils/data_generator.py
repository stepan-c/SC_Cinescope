#data_generator
from faker import Faker


class DataGenerator:
    faker = Faker("ru_RU")

    @staticmethod
    def generator_email():
        random_chars = ''.join(DataGenerator.faker.random_letters(length=4)).lower()
        return f"{random_chars}@email.com"


    @staticmethod
    def name_generator():
        return DataGenerator.faker.name()

    @staticmethod
    def password_generator():
        password = DataGenerator.faker.password(
            length=12,
            special_chars=False,
            digits=True,
            upper_case=True,
            lower_case=True
        )
        return password
    @staticmethod
    def generator_numbers():
        random_numbers = DataGenerator.faker.random_number(digits=4,fix_len= True)
        return random_numbers

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