from datetime import datetime
import datetime as dt
from pytz import timezone

import pytest

from api_testing_practice.utils.data_generator import DataGenerator
from db_requester.models import MovieDBModel, AccountTransactionTemplate


def test_create_delete_movie(api_manager, super_admin, db_session):
    # как бы выглядел SQL запрос
    """SELECT id, "name", price, description, image_url, "location", published, rating, genre_id, created_at
       FROM public.movies
       WHERE name='Test Moviej1h8qss9s5';"""

    # Извлекаем сессию из кортежа, который возвращает фикстура db_session
    session, test_user = db_session

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

    # Получаем токен из super_admin
    super_admin.api.session.headers.get('Authorization', '').replace('Bearer ', '')

    response = super_admin.api.movie_api.create_movies(
        movie_data=movie_data
    )
    assert response.status_code == 201, "Фильм должен успешно создаться"
    response_data = response.json()

    # проверяем после вызова api_manager.movie_api.create_movies в базе появился наш фильм
    movies_from_db = session.query(MovieDBModel).filter(MovieDBModel.name == movie_name)
    assert movies_from_db.count() == 1, "В базе уже присутствует фильм с таким названием"

    movie_from_db = movies_from_db.first()
    # можете обратить внимание что в базе данных есть поле created_at которое мы не задавали явно
    # наш сервис сам его заполнил. проверим что он заполнил его верно с погрешностью в 5 минут
    assert movie_from_db.created_at >= (datetime.now(timezone('UTC')).replace(tzinfo=None) - dt.timedelta(
        minutes=5)), "Сервис выставил время создания с большой погрешностью"

    # Берем айди фильма который мы только что создали и удаляем его из базы через апи
    # Удаляем фильм
    delete_response = super_admin.api.movie_api.delete_movies(
        movie_id=response_data["id"]
    )
    assert delete_response.status_code == 200, "Фильм должен успешно удалиться"

    # проверяем что в конце тестирования фильма с таким названием действительно нет в базе
    movies_from_db = session.query(MovieDBModel).filter(MovieDBModel.name == movie_name)
    assert movies_from_db.count() == 0, "Фильм не был удален из базы!"



def test_accounts_transaction_template(db_session):
    # ====================================================================== Подготовка к тесту
    # Извлекаем: сессию из кортежа
    session, test_user = db_session

    # Создаем новые записи в базе данных
    stan = AccountTransactionTemplate(user=f"Stan_{DataGenerator.generator_numbers()}", balance=999)
    bob = AccountTransactionTemplate(user=f"Bob_{DataGenerator.generator_numbers()}", balance=555)

    # Добавляем записи в сессию
    session.add_all([stan, bob])  # Фиксируем изменения в базе данных
    session.commit()

    def transfer_money(session, from_account, to_account, amount):
        # Получаем счета
        from_account = session.query(AccountTransactionTemplate).filter_by(user=from_account).one()
        to_account = session.query(AccountTransactionTemplate).filter_by(user=to_account).one()

        # Проверяем, что на счете достаточно средств
        if from_account.balance < amount:
            raise ValueError("Недостаточно средств на счете")

        # Выполняем перевод
        from_account.balance -= amount
        to_account.balance += amount

        # Сохраняем изменения
        session.commit()

    # ====================================================================== Тест
    # Проверяем начальные балансы
    assert stan.balance == 999
    assert bob.balance == 555

    try:
        # Выполняем перевод 111 единиц от stan к bob
        transfer_money(session, from_account=stan.user, to_account=bob.user, amount=111)

        # Проверяем, что балансы изменились
        assert stan.balance == 888
        assert bob.balance == 666

    except Exception as e:
        # Если произошла ошибка, откатываем транзакцию
        session.rollback()  # откат всех введеных нами изменений
        pytest.fail(f"Ошибка при переводе денег: {e}")

    finally:
        # Удаляем данные для тестирования из базы
        session.delete(stan)
        session.delete(bob)
        # Фиксируем изменения в базе данных
        session.commit()