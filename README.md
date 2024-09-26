# otus_hw5_api

# Цель:
Потренироваться тестировать API сервисы на основе их документации

# Описание:
# Часть 1
Нужно написать тесты для API следующих сервисов:

* https://dog.ceo/dog-api/
* https://www.openbrewerydb.org/
* https://jsonplaceholder.typicode.com/
Для каждого из указанных выше сервисов должны быть выполнены следующие условия:

Написать минимум 5 тестов для REST API сервиса
Как минимум 2 из 5 тестов должны использовать параметризацию
Документация к API есть на сайте
Тесты должны успешно проходить
Тестирование каждого API оформить в отдельном тестовом модуле

# Часть 2
Реализуйте в отдельном модуле (файле) тестовую функцию, которая будет принимать 2 параметра:

url - значение по умолчанию https://ya.ru
status_code - значение по умолчанию 200

Параметры должны быть реализованы через pytest.addoption. Можно положить фикcтуру и тестовую функцию в один файл. Основная задача чтобы ваш тест проверял статус ответа по переданному URL. Например, по несуществующему адресу https://ya.ru/sfhfh должен быть валидным ответ 404

# Пример запуска pytest:

test_module.py --url=https://mail.ru --status_code=200