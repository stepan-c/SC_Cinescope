from datetime import datetime
import datetime as dt
import allure
from pytz import timezone
import pytest
from api_testing_practice.utils.data_generator import DataGenerator
from db_requester.models import MovieDBModel, AccountTransactionTemplate


@allure.epic("Тестирование фильмов")
@allure.feature("Создание фильмов")

class TestCreateDeleteMovie:
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("qa", "s.cheshev")
    @allure.description("""
    Тест db создание и удаление фильма
    Шаги:
    1.Генерируем название фильма и проверяем его отсутствие в db
    2.Авторизуемся как супер админ, создаем фильм и проверяем на создание
    3.Проверяем наличие фильма в db
    4.Проверяем, что сервис правильно заполнил время создания
    5.Удаляем фильм из db и проверяем его отсутствие
    """)
    def test_create_delete_movie(self, api_manager, super_admin, db_session):

        # Извлекаем сессию из кортежа, который возвращает фикстура db_session
        session, test_user = db_session
        with allure.step("Генерируем название фильма и проверяем его отсутствие в db"):
            movie_name = f"Test Movie{DataGenerator.name_generator()}"
            movies_from_db = session.query(MovieDBModel).filter(MovieDBModel.name == movie_name)

            # проверяем что до начала тестирования фильма с таким названием нет
            assert movies_from_db.count() == 0, "В базе уже присутствует фильм с таким названием"

        movie_data = {
            "name": movie_name,
            "price": 500,
            "description": "Описание тестового фильма",
            "location": "MSK",
            "published": True,
            "genreId": 3
        }

        with allure.step("Авторизуемся как супер админ, создаем фильм и проверяем на создание"):
            # Получаем токен из super_admin
            super_admin.api.session.headers.get('Authorization', '').replace('Bearer ', '')

            response = super_admin.api.movie_api.create_movies(
                movie_data=movie_data
            )
            assert response.status_code == 201, "Фильм должен успешно создаться"
            response_data = response.json()

        with allure.step("Проверяем наличие фильма в db"):
            # проверяем после вызова api_manager.movie_api.create_movies в базе появился наш фильм
            movies_from_db = session.query(MovieDBModel).filter(MovieDBModel.name == movie_name)
            assert movies_from_db.count() == 1, "В базе уже присутствует фильм с таким названием"

        with allure.step("Проверяем, что сервис правильно заполнил время создания"):
            movie_from_db = movies_from_db.first()
            # можете обратить внимание что в базе данных есть поле created_at которое мы не задавали явно
            # наш сервис сам его заполнил. проверим что он заполнил его верно с погрешностью в 5 минут
            assert movie_from_db.created_at >= (datetime.now(timezone('UTC')).replace(tzinfo=None) - dt.timedelta(
                minutes=5)), "Сервис выставил время создания с большой погрешностью"

        with allure.step("Удаляем фильм из db и проверяем его отсутствие"):
            # Берем айди фильма который мы только что создали и удаляем его из базы через апи
            # Удаляем фильм
            delete_response = super_admin.api.movie_api.delete_movies(
                movie_id=response_data["id"]
            )
            assert delete_response.status_code == 200, "Фильм должен успешно удалиться"

            # проверяем что в конце тестирования фильма с таким названием действительно нет в базе
            movies_from_db = session.query(MovieDBModel).filter(MovieDBModel.name == movie_name)
            assert movies_from_db.count() == 0, "Фильм не был удален из базы!"


@allure.epic("Тестирование транзакций")
@allure.feature("Тестирование транзакций между счетами")
class TestAccountTransactionTemplate:

    @allure.story("Тест проверяет корректность перевода")
    @allure.description("""
    Шаги:
    1. Создание двух счетов: Bob и Stan
    2. Выполняем перевод между счетами
    3. Проводим проверку изменения счета
    4. Удаляем данные из db
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("qa", "s.cheshev")

    def test_accounts_transaction_template(self, db_session):

        session, test_user = db_session

        with allure.step("Создание двух счетов: Bob и Stan"):
            stan = AccountTransactionTemplate(user=f"Stan_{DataGenerator.generator_numbers()}", balance=999)
            bob = AccountTransactionTemplate(user=f"Bob_{DataGenerator.generator_numbers()}", balance=555)

            session.add_all([stan, bob])
            session.commit()

        def transfer_money(session, from_account, to_account, amount):
            with allure.step("Получаем счета"):
                from_account = session.query(AccountTransactionTemplate).filter_by(user=from_account).one()
                to_account = session.query(AccountTransactionTemplate).filter_by(user=to_account).one()

            with allure.step("Проверяем что на счете достаточно средств"):
                if from_account.balance < amount:
                    raise ValueError("Недостаточно средств на счете")

            with allure.step("Логика изменения балансов"):
                from_account.balance -= amount
                to_account.balance += amount

                session.commit()

        with allure.step("Проверяем начальные балансы"):
            assert stan.balance == 999
            assert bob.balance == 555

        try:
            with allure.step("Выполняем перевод"):
                transfer_money(session, from_account=stan.user, to_account=bob.user, amount=111)

            with allure.step("Проверяем, что баланс изменился"):

                assert stan.balance == 888
                assert bob.balance == 666

        except Exception as e:
            # Если произошла ошибка, откатываем транзакцию
            session.rollback()  # откат всех введеных нами изменений
            pytest.fail(f"Ошибка при переводе денег: {e}")

        finally:
            with allure.step("Удаляем данные для тестирования из базы"):
                session.delete(stan)
                session.delete(bob)
                # Фиксируем изменения в базе данных
                session.commit()