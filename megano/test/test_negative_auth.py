# Тест на авторизацию пользователя с неподходящим "E-mail" или с неподходящим "Пароль".
# Делается после регистрации с валидными данными.

import logging
import yaml, time
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
megano = Site(testdata["address"])
name = testdata["true_username"]
email = testdata["true_email"]
password = testdata["true_password"]
phone_number = testdata["true_number"]

logging.basicConfig(filename="mylog.log")

def test_authorization2(btn_entrance, field_username, field_id_password,
                        btn_enter, btn_save, text_not_match):
    logging.info("Test unsuccessful authorization1")
    click_entrance = megano.find_element("xpath", btn_entrance)
    click_entrance.click()
    time.sleep(1)
    # вводим неправильный "E-mail"
    input_field_username = megano.find_element("css", field_username)
    input_field_username.clear()
    input_field_username.send_keys("5321@mail.ru")
    time.sleep(1)
    # вводим правильный "Пароль", с которым успешно зарегистрировались
    input_field_id_password = megano.find_element("css", field_id_password)
    input_field_id_password.clear()
    input_field_id_password.send_keys(password)
    time.sleep(1)
    click_btn_enter = megano.find_element("xpath", btn_enter)
    click_btn_enter.click()
    time.sleep(1)
    not_match = megano.find_element("xpath", text_not_match)
    text = not_match.text
    logging.info("We were unable to log into your profile")
    assert text == "Your email and password didn't match. Please try again."

def test_authorization2_1(field_username, field_id_password,
                        btn_enter, btn_save, text_not_match):
    logging.info("Test unsuccessful authorization2")
    # вводим правильный "E-mail", с которым успешно зарегистрировались
    input_field_username = megano.find_element("css", field_username)
    input_field_username.clear()
    input_field_username.send_keys(email)
    time.sleep(1)
    # вводим неправильный "Пароль"
    input_field_id_password = megano.find_element("css", field_id_password)
    input_field_id_password.clear()
    input_field_id_password.send_keys("TopGear1111")
    time.sleep(1)
    click_btn_enter = megano.find_element("xpath", btn_enter)
    click_btn_enter.click()
    time.sleep(1)
    not_match = megano.find_element("xpath", text_not_match)
    text = not_match.text
    megano.close()
    logging.info("We were unable to log into your profile")
    assert text == "Your email and password didn't match. Please try again."

# Вход в профиль не должен произойти ни в одном из двух случаев.
# Если произошло любое другое действие, кроме появления фразы Your email and password didn't match. Please try again.,
# то тест не прошел.
# Имеется скриншот.
