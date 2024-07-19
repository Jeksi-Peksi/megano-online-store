# Бонусный тест на работу поисковой строки.

import logging
import yaml, time
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
megano = Site(testdata["address"])

logging.basicConfig(filename="mylog.log")

def test_search(btn_search, btn_megano_emage, text_navigation):
    logging.info("Test search")
    # Просто кликаем на логотип "Megano", который также является кнопкой загрузки главной страницы.
    megano_logo = megano.find_element("xpath", btn_megano_emage)
    megano_logo.click()
    time.sleep(1)
    # Кликаем на кнопку "Поиск" рядом с поисковой строкой в центре главной страницы.
    search = megano.find_element("xpath", btn_search)
    search.click()
    time.sleep(2)
    # Ищем текст "НАВИГАЦИЯ" в подвале сайта, который всегда в одном и том же месте на любой странице.
    navigation = megano.find_element("xpath", text_navigation)
    text = navigation.text
    megano.close()
    logging.error("Код ошибки 403")
    assert text == "НАВИГАЦИЯ"

# Тест не прошел и сайт вылетел в ошибку 403.
# Поиск на сайте невозможен (имеется скриншот)
