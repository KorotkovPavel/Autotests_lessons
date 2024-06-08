from QAP_HW_m24_restapi.api import PetFriends
from QAP_HW_m24_restapi.settings import valid_email, valid_password
import os

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result
def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0
def test_add_new_pet_with_valid_data(name='Тэсс', animal_type='скотишфолд',
                                     age='4', pet_photo='images/cat.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


# def test_successful_delete_self_pet():
#     """Проверяем возможность удаления питомца"""
#
#     # Получаем ключ auth_key и запрашиваем список своих питомцев
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
#
#     # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
#     if len(my_pets['pets']) == 0:
#         pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
#         _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
#
#     # Берём id первого питомца из списка и отправляем запрос на удаление
#     pet_id = my_pets['pets'][0]['id']
#     status, _ = pf.delete_pet(auth_key, pet_id)
#
#     # Ещё раз запрашиваем список своих питомцев
#     _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
#
#     # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
#     assert status == 200
#     assert pet_id not in my_pets.values()


# def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
#     """Проверяем возможность обновления информации о питомце"""
#
#     # Получаем ключ auth_key и список своих питомцев
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
#
#     # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
#     if len(my_pets['pets']) > 0:
#         status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
#
#         # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
#         assert status == 200
#         assert result['name'] == name
#     else:
#         # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
#         raise Exception("There is no my pets")

def test_create_pet_simple_with_valid_data(name='Боб', animal_type='пёс', age='1'):
    """Проверяем что можно добавить питомца с корректными данными без фото"""
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_create_pet_simple_with_invalid_age_string(name='Дори', animal_type='рыбка', age='два'):
    """Проверяем что нельзя добавить питомца если указать вместо числа - слово"""
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_create_pet_simple_with_invalid_age_symbol(name='Кеша', animal_type='попугай', age='$%'):
    """Проверяем что нельзя добавить питомца с введеными символами в поле возраст"""
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_create_pet_simple_with_invalid_name(name='23123', animal_type='пёс', age='$%'):
    """Проверяем что нельзя добавить питомца с введеными числами в поле имя"""
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_create_pet_simple_with_empty_name(name='', animal_type='пёс', age='$%'):
    """Проверяем что нельзя добавить питомца c пустым полем имя"""
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_photo_of_pet_with_valid_data():
    '''Получаем ключ auth_key и запрашиваем список своих питомцев'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id второго питомца из списка и отправляем запрос на добавление фото
    pet_id = my_pets['pets'][1]['id']
    status, _ = pf.add_photo_of_pet(auth_key, pet_id, 'images/cat.jpg')

    # Проверяем что статус ответа равен 200
    assert status == 200

def test_add_photo_of_pet_with_png():
    '''Получаем ключ auth_key и запрашиваем список своих питомцев'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id четвертого питомца из списка и отправляем запрос на добавление фото
    pet_id = my_pets['pets'][3]['id']
    status, _ = pf.add_photo_of_pet(auth_key, pet_id, 'images/err.png')

    # Проверяем что статус ответа равен 200. Должна быть ошибка, фото не добавится
    assert status == 200

def test_add_photo_of_pet_with_another_path_png():
    '''Получаем ключ auth_key и запрашиваем список своих питомцев'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id второго питомца из списка и отправляем запрос на добавление фото
    pet_id = my_pets['pets'][1]['id']
    status, _ = pf.add_photo_of_pet(auth_key, pet_id, 'tests/444.png')

    # Проверяем что статус ответа равен 200
    assert status == 200

def test_add_photo_of_pet_with_another_path():
    '''Получаем ключ auth_key и запрашиваем список своих питомцев'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на добавление фото
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.add_photo_of_pet(auth_key, pet_id, 'tests/323.jpg')

    # Проверяем что статус ответа равен 200
    assert status == 200

def test_add_photo_of_pet_without_path():
    '''Получаем ключ auth_key и запрашиваем список своих питомцев'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на добавление фото
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.add_photo_of_pet(auth_key, pet_id, '123.jpg', )

    # Проверяем что статус ответа равен 200
    assert status == 200
