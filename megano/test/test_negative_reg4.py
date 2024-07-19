# 2-й тест на регистрацию пользователя с вводом невалидных данных в поле "E-mail"
# E-mail состоит из множества Русских букв и цифр. (РуссКиЕбуквЫ321235@yandex.ru)
# Остальные данные валидные

import logging
import yaml, time
from module import Site


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
megano = Site(testdata["address"])
name = testdata["invalid_input1"]
password = testdata["true_password"]
phone_number = testdata["true_number"]

def test_registration4(btn_default_registration, field_name, field_email, field_password,
                       btn_registration1, field_phone_number, btn_save, text_successful_save):
    logging.info("Test negative registration4 (E-mail)")
    click_registration = megano.find_element("xpath", btn_default_registration)
    click_registration.click()
    time.sleep(2)
    input_field_name = megano.find_element("css", field_name)
    input_field_name.clear()
    input_field_name.send_keys(name)
    time.sleep(2)
    input_field_email = megano.find_element("css", field_email)
    input_field_email.clear()
    # Емейл только из русских букв разного регистра и цифр.
    input_field_email.send_keys("РуссКиЕбуквЫ321235@yandex.ru")
    time.sleep(2)
    input_field_password = megano.find_element("css", field_password)
    input_field_password.clear()
    input_field_password.send_keys(password)
    time.sleep(2)
    click_registration1 = megano.find_element("xpath", btn_registration1)
    click_registration1.click()
    time.sleep(2)
    input_field_phone_number = megano.find_element("css", field_phone_number)
    input_field_phone_number.clear()
    input_field_phone_number.send_keys(phone_number)
    time.sleep(2)
    click_save = megano.find_element("xpath", btn_save)
    click_save.click()
    time.sleep(2)
    profile_save = megano.find_element("css", text_successful_save)
    text = profile_save.text
    megano.close()
    assert text == "Профиль успешно сохранен"

# При успешной регистрации с невалидными данными в поле "Имя" тест пройдёт.
# При неуспешной регистрации появится alert и тест не пройдёт.
# В данном случае появляется надпись о том, что необходимо убрать русскую букву "Р". (и далее так со всеми)
# Имеется скриншот.
