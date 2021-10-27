from Pet_friends.api import PetApi
from Pet_friends.settings import valid_email, valid_password, invalid_email, invalid_password
import os


pf = PetApi()


def test_get_api_key_valid(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result

def test_get_api_pets_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_api_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

def test_post_api_pets_valid(name='Кот', animal_type='Домашний Кот', age='0.4', pet_photo='image\cat1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.post_api_pets(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_delete_api_pets_valid(filter='my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, first_list = pf.get_api_pets(auth_key, filter)
    pet_id = first_list['pets'][0]['id']
    status = pf.delete_ape_pet(auth_key, pet_id)
    _, second_list = pf.get_api_pets(auth_key, filter)

    assert status == 200
    assert first_list['pets'][0]['id'] != second_list['pets'][0]['id']

def test_put_api_pets_valid(filter='my_pets', name='Kit', animal_type='Home Kit', age='0.8'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, first_list = pf.get_api_pets(auth_key, filter)
    pet_id = first_list['pets'][0]['id']
    status, result = pf.put_api_pets(auth_key, pet_id, name, animal_type, age)
    _, second_list = pf.get_api_pets(auth_key, filter)

    assert status == 200
    assert first_list['pets'][0] != second_list['pets'][0]


def test_post_api_pets_without_photo_valid(name='Gosha', animal_type='Dog', age='13'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['pet_photo'] == ''


def test_post_api_pets_set_photo_valid(filter='my_pets', pet_photo='image\parrot1.png'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, first_list = pf.get_api_pets(auth_key, filter)
    pet_id = first_list['pets'][0]['id']
    status, result = pf.post_api_pets_set_photo(auth_key, pet_id, pet_photo)

    assert status == 200
    assert result['pet_photo'] != ''


#Негативные тесты

def test_get_api_key_with_invalid_data(email=invalid_email, password=invalid_password):
    status, _ = pf.get_api_key(email, password)

    assert status == 403


def test_get_api_pets_with_invalid_key(filter=''):
    auth_key = {}
    auth_key['key'] = 'gdgdg234dfg21'
    status, _ = pf.get_api_pets(auth_key, filter)

    assert status == 403


def test_get_api_pets_with_invalid_filter(filter='all_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, _ = pf.get_api_pets(auth_key, filter)

    assert status != 200


def test_post_api_pets_without_any_info(name='', animal_type='', age='', pet_photo='image\parrot1.png'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert result['name'] == name
'''Тест провален, т.к. получается запостить питомца с невалидной информацией. Ожидаемый результат, что код статуса будет = 400'''


def test_post_api_pets_without_photo_invalid(name='', animal_type='', age=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert result['pet_photo'] == ''
'''Тест провален, т.к. получается запостить питомца с невалидной информацией. Ожидаемый результат, что код статуса будет = 400'''


def test_put_api_pets_with_invalid_pet_id(filter='my_pets', name='Kit', animal_type='Home Kit', age='0.8'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, first_list = pf.get_api_pets(auth_key, filter)
    pet_id = first_list['pets'][0]['id']+'fdg4234'
    status, _ = pf.put_api_pets(auth_key, pet_id, name, animal_type, age)

    assert status == 400


def test_put_api_pets_without_any_info(filter='my_pets', name='', animal_type='', age=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, first_list = pf.get_api_pets(auth_key, filter)
    pet_id = first_list['pets'][0]['id']
    status, _ = pf.put_api_pets(auth_key, pet_id, name, animal_type, age)

    assert status != 200


def test_post_api_pets_simple_with_str_in_age(name='Pet', animal_type='Kot', age='stodvaccactri'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert result['pet_photo'] == ''


def test_delete_api_pets_with_invalid_pet_id(filter='my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, first_list = pf.get_api_pets(auth_key, filter)
    pet_id = first_list['pets'][0]['id']+'1242ddffgd'
    status = pf.delete_ape_pet(auth_key, pet_id)

    assert status != 200


def test_put_api_pets_change_info_someone_pet(filter='', name='Change', animal_type='Alien', age='Pet'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, first_list = pf.get_api_pets(auth_key, filter)
    pet_id = first_list['pets'][1]['id']
    status, _ = pf.put_api_pets(auth_key, pet_id, name, animal_type, age)

    assert status != 200
'''Тест провален, т.к. попытка изменить не своего питомца удалась. Такой функиональности на сайте нет'''