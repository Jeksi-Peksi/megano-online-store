# Тест на регистрацию пользователя с вводом невалидных данных в поле "Имя", остальные данные валидные

import logging
import yaml, time
from module import Site


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
megano = Site(testdata["address"])
name = testdata["invalid_input1"]
password = testdata["true_password"]
phone_number = testdata["true_number"]

def test_registration2(btn_default_registration, field_name, field_email, field_password, btn_registration1, field_phone_number, btn_save, text_successful_save):
    logging.info("Test negative registration2 (Name)")
    click_registration = megano.find_element("xpath", btn_default_registration)
    click_registration.click()
    time.sleep(2)
    input_field_name = megano.find_element("css", field_name)
    input_field_name.clear()
    input_field_name.send_keys(name)
    time.sleep(2)
    input_field_email = megano.find_element("css", field_email)
    input_field_email.clear()
    input_field_email.send_keys("123456789@mail.ru")
    time.sleep(2)
    input_field_password = megano.find_element("css", field_password)
    input_field_password.clear()
    input_field_password.send_keys(password)
    time.sleep(2)
    click_registration1 = megano.find_element("xpath", btn_registration1)
    click_registration1.click()
    time.sleep(2)
    logging.info("Click registration button")
    input_field_phone_number = megano.find_element("css", field_phone_number)
    input_field_phone_number.clear()
    input_field_phone_number.send_keys("+7 (999) 999-99-92")
    time.sleep(2)
    click_save = megano.find_element("xpath", btn_save)
    click_save.click()
    time.sleep(2)
    profile_save = megano.find_element("css", text_successful_save)
    text = profile_save.text
    logging.info("Профиль успешно сохранен")
    megano.close()
    assert text == "Профиль успешно сохранен"

# При успешной регистрации с невалидными данными в поле "Имя" тест пройдёт.
# При неуспешной регистрации появится alert и тест не пройдёт.
# В данном случае регистрация проходит успешно и мы после ввода данных переходим на страницу профиля пользователя.
# Имеется скриншот.
