from api import PetFriends

from settings import valid_email, valid_password, valid_email_1, valid_password_1, valid_email_2, valid_password_2

import os


pf = PetFriends()

# тест 1
def test_add_new_pet_with_not_valid_data_negative1(name='Муся', animal_type='Английская',
                                     age='-2', pet_photo='images/cat1.jpg'):
    """Проверяем, что нельзя добавить питомца с отриательным возрастом"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    """получен ответ со статусом кода 200, питомец с отрицательным возрастом появилсля в списке питомцев"""
# тест 2
def test_add_new_pet_with_not_valid_data_negative2(name='::Муся№;1223%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%!!!',
                                              animal_type='Английская', age='2', pet_photo='images/cat1.jpg'):
    """Проверяем, что нельзя добавить питомца с именем, состоящего из цифр и иных символов, а так же большим
    количеством символов"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    """получен ответ со статусом кода 400, однако питомец с данным именем все равно добавился в список питомцев"""

# тест 3

def test_add_new_pet_with_not_valid_data_negative3(name='', animal_type='', age='', pet_photo='images/cat1.jpg'):
    """Проверяем, что нельзя добавить питомца с пустыми значениями во всех полях: имя, порода, возраст питомца, только с фото"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    """получен ответ со статусом кода 400, однако питомец с пустыми значениями и с фото добавился в список питомцев"""

# тест 4

def test_add_new_pet_with_not_valid_data_negative4(name='1234', animal_type='1234', age='фбс', pet_photo='images/cat1.jpg'):
    """Проверяем, что нельзя добавить питомца с цифрами во всех полях: имя, порода и буквами в поле возраст питомца"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    """вместо ответа со статусом 400, получен ответ со статусом кода 200, питомец добавился в список питомцев"""

# тест 5

def test_add_new_pet_with_not_valid_data_negative5(name='1234', animal_type='1234', age='фбс', pet_photo='images/jag.jpg'):
    """Проверяем, что нельзя добавить питомца с цифрами во всех полях: имя, порода и буквами в поле возраст питомца"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 000
    """вместо ответа со статусом 400, получен ответ со статусом кода 200, питомец добавился в список питомцев"""

# тест 6

def test_add_new_pet_with_not_valid_data_negative6(name='Henry', animal_type='Dog', age='10', pet_photo='images/grt.pdf'):
    """Проверяем, что нельзя добавить питомца с фото иного формата"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    """получен ответ со статусом кода 200, однако питомец добавился в список питомцев, но без фото формата пдф"""

# тест 7

def test_get_api_key_for_not_valid_user(email=valid_email_1, password=valid_password_1):
    """ Проверяем что введенный email = Melory27yandex.ru не корректен """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' in result
"""ответ приходит с ошибкой 403"""

# тест 8

def test_get_api_key_for_not_valid_user_1(email=valid_email_2, password=valid_password_2):
    """Проверяем что при вводе неправильного пароля выдает ошибку"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' in result
"""ответ приходит с ошибкой 403"""

# тест 9

def test_add_new_pet_with_not_valid_data_negative9(name='Donna', animal_type='cat', age='2232325436546476475756756756'):
    """Проверяем, что нельзя добавить питомца без фото с большим количеством символов в поле возраст"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    """получен ответ со статусом кода 200, питомец  без фото с большим количеством символов в поле возраст
     добавился в список питомцев"""

# тест 10

def test_add_new_pet_with_not_valid_data_negative10(name='Donna', animal_type='2343№№65667657876867867696945ака', age='22'):
    """Проверяем, что нельзя добавить питомца без фото с большим количеством различных символов в поле порода"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    """получен ответ со статусом кода 400, однако питомец  без фото с большим количеством символов в поле порода
     добавился в список питомцев"""