import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(executable_path=r'C:\Kirill\Proga\BrowsersDrivers\chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('basarab.kirill00@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('KL12283288kl')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Заходим на вкладку "мои питомцы"
    pytest.driver.find_element_by_xpath(r'//a[@href="/my_pets"]').click()

    yield

    pytest.driver.quit()


def test_amount_of_pets():
    # Получаем данные пользователя
    user_data = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]')))
    amount_of_cards = pytest.driver.find_elements_by_xpath('//tbody/tr')

    # Находим количество питомце, которое указано в данных пользователя
    amount_of_pets = int(user_data.text.split()[2])

    #Сравниваем число питомцев с числом карточек
    assert amount_of_pets == len(amount_of_cards)


def test_pets_with_photo():
    # Получаем данные с карточек питомцев
    images = pytest.driver.find_elements_by_xpath(r'//tbody/tr/th/img')

    # Заводим переменную для отслеживания фото
    pet_with_photo = 0

    # Считаем количество питомцев с фото
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            pet_with_photo += 1

    # Проверям наличие фото хотя бы у половины питомцев
    assert pet_with_photo >= round(len(images) / 2)


def test_pets_attributes():
    # Добавляем ожидание, что на странице будут присутствовать хотя бы 1 карточка питомца
    pytest.driver.implicitly_wait(5)

    # Получаем данные с карточек питомцев
    names_data = pytest.driver.find_elements_by_xpath(r'//tbody/tr/td[1]')
    breed = pytest.driver.find_elements_by_xpath(r'//tbody/tr/td[2]')
    age = pytest.driver.find_elements_by_xpath(r'//tbody/tr/td[3]')

    # Проверяем наличие имени, породы и возраста у каждого питомца
    for i in range(len(names_data)):
        assert names_data[i].text != ''
        assert breed[i].text != ''
        assert age[i].text != ''


def test_unique_name():
    # Получаем данные с карточек питомцев
    names_data = pytest.driver.find_elements_by_xpath(r'//tbody/tr/td[1]')

    # Создаем массив имен питомцев
    names = []
    for i in range(len(names_data)):
        names.append(names_data[i].text)

    # Проверяем уникальность имён питомцев
    for i in range(len(names)):
        assert names.count(names[i]) == 1


def test_unique_pets():
    # Получаем данные с карточек питомцев
    names_data = pytest.driver.find_elements_by_xpath(r'//tbody/tr/td[1]')
    breed = pytest.driver.find_elements_by_xpath(r'//tbody/tr/td[2]')
    age = pytest.driver.find_elements_by_xpath(r'//tbody/tr/td[3]')

    # Создаём массив с данными каждого питомца
    pets_data = []
    for i in range(len(names_data)):
        pets_data.append((names_data[i].text, breed[i].text, age[i].text))

    # Проверяем уникальность питомцев
    for i in range(len(pets_data)):
        assert pets_data.count(pets_data[i]) == 1