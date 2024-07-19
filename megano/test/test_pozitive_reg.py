# Тест на регистрацию нового пользователя с валидными данными.

import logging
import yaml, time
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
megano = Site(testdata["address"])
name = testdata["true_username"]
email = testdata["true_email"]
password = testdata["true_password"]
phone_number = testdata["true_number"]

logging.basicConfig(filename="mylog.log")

def test_pozitive_registration(btn_entrance, btn_registration, field_name, field_email, field_password,
                               btn_registration1, field_phone_number, btn_save, text_successful_save):
    logging.info("Test pozitive registration")
    click_entrance = megano.find_element("xpath", btn_entrance)
    click_entrance.click()
    time.sleep(1)
    click_registration = megano.find_element("xpath", btn_registration)
    click_registration.click()
    time.sleep(1)
    input_field_name = megano.find_element("css", field_name)
    input_field_name.clear()
    input_field_name.send_keys(name)
    time.sleep(1)
    input_field_email = megano.find_element("css", field_email)
    input_field_email.clear()
    input_field_email.send_keys(email)
    time.sleep(1)
    input_field_password = megano.find_element("css", field_password)
    input_field_password.clear()
    input_field_password.send_keys(password)
    time.sleep(1)
    click_registration1 = megano.find_element("xpath", btn_registration1)
    click_registration1.click()
    time.sleep(1)
    input_field_phone_number = megano.find_element("css", field_phone_number)
    input_field_phone_number.clear()
    input_field_phone_number.send_keys(phone_number)
    time.sleep(1)
    click_save = megano.find_element("xpath", btn_save)
    click_save.click()
    time.sleep(1)
    profile_save = megano.find_element("css", text_successful_save)
    text = profile_save.text
    megano.close()
    logging.info("We have completed registration")
    assert text == "Профиль успешно сохранен"

# При успешной регистрации с валидными данными тест пройдёт.
# Произойдёт это в том случае, когда будет завершена регистрация и прожата кнопка "Сохранить".
# Появится надпись "Профиль успешно сохранен".
# Имеется скриншот.
