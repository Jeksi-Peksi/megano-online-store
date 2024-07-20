# Тест на регистрацию пользователя с вводом невалидных данных в поля "Имя" и "Пароль" по-очереди.
# Вводим в поля "Имя" и "Пароль" по очереди одни пробелы (допустим, по 10).
# Остальные данные валидные.

import logging
import yaml, time
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
megano = Site(testdata["address"])

def test_registration5(btn_default_registration, field_name, field_email, field_password, btn_registration1, text_required_field2):
    logging.info("Test negative registration5 (password = spaces)")
    click_registration = megano.find_element("xpath", btn_default_registration)
    click_registration.click()
    time.sleep(1)
    # Имя валидное
    input_field_name = megano.find_element("css", field_name)
    input_field_name.clear()
    input_field_name.send_keys("Привет")
    time.sleep(1)
    # Email валидный
    input_field_email = megano.find_element("css", field_email)
    input_field_email.clear()
    input_field_email.send_keys("123456789@yandex.ru")
    time.sleep(1)
    input_field_password = megano.find_element("css", field_password)
    input_field_password.clear()
    # Пароль из десяти пробелов
    input_field_password.send_keys("          ")
    time.sleep(1)
    logging.info("The password consists of only spaces")
    click_registration1 = megano.find_element("xpath", btn_registration1)
    click_registration1.click()
    time.sleep(1)
    required_field2 = megano.find_element("xpath", text_required_field2)
    text = required_field2.text
    assert text == "*Обязательное поле."

def test_registration5_1(field_name, field_email, field_password, btn_registration1, text_required_field1):
    logging.info("Test negative registration5_1 (The name consists of only spaces.)")
    # Имя невалидное (состоит из 10-ти пробелов)
    input_field_name = megano.find_element("css", field_name)
    input_field_name.clear()
    input_field_name.send_keys("          ")
    time.sleep(1)
    # Email валидный
    input_field_email = megano.find_element("css", field_email)
    input_field_email.clear()
    input_field_email.send_keys("123456789@yandex.ru")
    time.sleep(1)
    input_field_password = megano.find_element("css", field_password)
    input_field_password.clear()
    # Пароль валидный
    input_field_password.send_keys("Privet12345")
    time.sleep(1)
    click_registration1 = megano.find_element("xpath", btn_registration1)
    click_registration1.click()
    time.sleep(1)
    required_field1 = megano.find_element("xpath", text_required_field1)
    text = required_field1.text
    logging.info("увидели *Обязательное поле")
    megano.close()
    assert text == "*Обязательное поле."


# В данном случае сделаем наоборот. Если тест проходит, то пароль из пробелов невалидный.
# Регистрация не должна пройти.
# В данном случае появляется надпись под полем пароля (* Обязательное поле).
# Имеется скриншот.
