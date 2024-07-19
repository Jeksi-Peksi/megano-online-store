# Тест на авторизацию пользователя с валидными данными.
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

def test_authorization1(btn_entrance, field_username, field_id_password,
                        btn_enter, btn_save, successful_entrance):
    logging.info("Test successful authorization")
    click_entrance = megano.find_element("xpath", btn_entrance)
    click_entrance.click()
    time.sleep(1)
    input_field_username = megano.find_element("css", field_username)
    input_field_username.clear()
    input_field_username.send_keys(email)
    time.sleep(1)
    input_field_id_password = megano.find_element("css", field_id_password)
    input_field_id_password.clear()
    input_field_id_password.send_keys(password)
    time.sleep(1)
    click_btn_enter = megano.find_element("xpath", btn_enter)
    click_btn_enter.click()
    time.sleep(1)
    profile_save = megano.find_element("xpath", successful_entrance)
    text = profile_save.text
    megano.close()
    logging.info("We entered profile")
    assert text == "Аватар"

# Должен произойти вход в профиль, в личном кабинете которого можно увидеть поле с названием "Аватар".
# Если вход не произошел или слово "Аватар" не было найдено, то тест не пройдёт.
# Имеется скриншот.
