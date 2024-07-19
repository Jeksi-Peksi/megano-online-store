# Тест на регистрацию пользователя с незаполнением всех полей или части полей.

import logging
import yaml, time
from module import Site


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    megano = Site(testdata["address"])
    name = testdata["true_username"]
    email = testdata["true_email"]
    password = testdata["true_password"]
    phone_number = testdata["invalid_number"]
def test_registration1(btn_default_registration, field_name, field_email, field_password,
                       btn_registration1, field_phone_number, btn_save, text_successful_save):
    logging.info("Test negative registration1 (All fields are empty)")
    click_registration = megano.find_element("xpath", btn_default_registration)
    click_registration.click()
    time.sleep(1)
    input_field_name = megano.find_element("css", field_name)
    input_field_name.clear()
    input_field_name.send_keys()
    time.sleep(1)
    input_field_email = megano.find_element("css", field_email)
    input_field_email.clear()
    input_field_email.send_keys()
    time.sleep(1)
    input_field_password = megano.find_element("css", field_password)
    input_field_password.clear()
    input_field_password.send_keys()
    time.sleep(1)
    click_registration1 = megano.find_element("xpath", btn_registration1)
    click_registration1.click()
    time.sleep(1)
    logging.info("Registration failed")
    # проверяем только с заполненным полем "Имя"
    logging.info("Fields 'E-mail' and 'Пароль' are empty")
    input_field_name = megano.find_element("css", field_name)
    input_field_name.clear()
    input_field_name.send_keys(name)
    click_registration1 = megano.find_element("xpath", btn_registration1)
    click_registration1.click()
    time.sleep(1)
    logging.info("Registration failed")
    # проверяем только с заполненным полем "E-mail"
    logging.info("fields 'Имя' and 'Пароль' are empty")
    input_field_name = megano.find_element("css", field_name)
    input_field_name.clear()
    time.sleep(1)
    input_field_email = megano.find_element("css", field_email)
    input_field_email.clear()
    input_field_email.send_keys(email)
    time.sleep(1)
    click_registration1 = megano.find_element("xpath", btn_registration1)
    click_registration1.click()
    time.sleep(1)
    logging.info("Registration failed")
    # проверяем только с заполненным полем "Пароль"
    logging.info("fields 'Имя' and 'E-mail' are empty")
    input_field_name = megano.find_element("css", field_name)
    input_field_name.clear()
    time.sleep(1)
    input_field_email = megano.find_element("css", field_email)
    input_field_email.clear()
    time.sleep(1)
    input_field_password = megano.find_element("css", field_password)
    input_field_password.clear()
    input_field_password.send_keys(password)
    time.sleep(1)
    click_registration1 = megano.find_element("xpath", btn_registration1)
    click_registration1.click()
    time.sleep(1)
    logging.info("Registration failed")
    # проверяем только с заполненными полями "Имя" и "E-mail" без "Пароль"
    logging.info("field 'Пароль' is empty")
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
    time.sleep(1)
    click_registration1 = megano.find_element("xpath", btn_registration1)
    click_registration1.click()
    time.sleep(1)
    logging.info("Registration failed")
    # проверяем только с заполненными полями "Имя" и "Пароль" без "E-mail"
    logging.info("field 'E-mail' is empty")
    input_field_name = megano.find_element("css", field_name)
    input_field_name.clear()
    input_field_name.send_keys(name)
    time.sleep(1)
    input_field_email = megano.find_element("css", field_email)
    input_field_email.clear()
    time.sleep(1)
    input_field_password = megano.find_element("css", field_password)
    input_field_password.clear()
    input_field_password.send_keys(password)
    time.sleep(1)
    click_registration1 = megano.find_element("xpath", btn_registration1)
    click_registration1.click()
    time.sleep(1)
    logging.info("Registration failed")
    # проверяем только с заполненными полями "E-mail" и "Пароль" без "Имя"
    logging.info("field 'Имя' is empty")
    input_field_name = megano.find_element("css", field_name)
    input_field_name.clear()
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
    logging.info("Registration failed")
    #дальше проверка на проходимость этой страницы. Если не нашли поле номера, то регистрация не может продолжиться.
    logging.info("Еrying to find the phone number field")
    input_field_phone_number = megano.find_element("css", field_phone_number)
    input_field_phone_number.clear()
    input_field_phone_number.send_keys()
    time.sleep(2)
    click_save = megano.find_element("xpath", btn_save)
    click_save.click()
    time.sleep(2)
    profile_save = megano.find_element("css", text_successful_save)
    text = profile_save.text
    megano.close()
    logging.info("We have completed registration")
    assert text == "Профиль успешно сохранен"

# При успешной регистрации без ввода данных в поля тест пройдёт.
# При неуспешной регистрации появится alert и тест не пройдёт.
# В данном случае появляется надпись "Заполните это поле" под самым верхним пустым полем.
# Имеется скриншот.
