# Тест на регистрацию с заполнением во всех полях одной буквой.
# В нашем случае буква "d".

import logging
import yaml
import time
from module import Site


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
megano = Site(testdata["address"])

def test_registration6(btn_default_registration, field_name, field_email, field_password, btn_registration1, field_phone_number, btn_save, text_similar_name, text_short_pass):
    logging.info("Test negative registration6 (only one letter")
    click_registration = megano.find_element("xpath", btn_default_registration)
    click_registration.click()
    time.sleep(1)
    # Имя состоит только из одной буквы
    input_field_name = megano.find_element("css", field_name)
    input_field_name.clear()
    input_field_name.send_keys("d")
    time.sleep(1)
    # Email состоит только из одной буквы
    input_field_email = megano.find_element("css", field_email)
    input_field_email.clear()
    input_field_email.send_keys("d@gmail.com")
    time.sleep(1)
    input_field_password = megano.find_element("css", field_password)
    input_field_password.clear()
    # Пароль состоит только из одной буквы
    input_field_password.send_keys("d")
    time.sleep(1)
    click_registration1 = megano.find_element("xpath", btn_registration1)
    click_registration1.click()
    time.sleep(1)
    similar_name = megano.find_element("xpath", text_similar_name)
    text = similar_name.text
    short_password = megano.find_element("xpath", text_short_pass)
    text_pass = short_password.text
    logging.info("*Введённый пароль слишком похож на Имя пользователя.")
    megano.close()
    assert (text == "*Введённый пароль слишком похож на Имя пользователя." and text_pass == "*Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.")

# Если тест проходит, то мы увидели появившиеся алерты. И дальнейшая регистрация невозможна.
# 1-й с текстом: "*Введённый пароль слишком похож на Имя пользователя."
# 2-й с текстом: "*Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов."
