import pytest
import logging

@pytest.fixture()
def btn_entrance():
    return """/html/body/header/header/div[1]/div/div/nav/div/div/a[1]"""
@pytest.fixture()
def btn_default_registration():
    return """/html/body/header/header/div[1]/div/div/nav/div/div/a[2]"""
@pytest.fixture()
def btn_registration():
    return """/html/body/main/main/div[2]/div[2]/form/a[2]"""
@pytest.fixture()
def field_name():
    return """#username"""
@pytest.fixture()
def field_email():
    return """#email"""
@pytest.fixture()
def field_password():
    return """#password"""
@pytest.fixture()
def btn_registration1():
    return """/html/body/main/main/div[2]/div[2]/form/input[2]"""
@pytest.fixture()
def field_phone_number():
    return """#phone"""
@pytest.fixture()
def btn_save():
    return """/html/body/main/div/div/div/div[2]/div/form/div/div[2]/div[5]/div[1]/button"""
@pytest.fixture()
def text_successful_save():
    return """body > main > div > div > div > div.Section-content > div > form > div > div:nth-child(2) > div:nth-child(8) > div.Profile-success"""
@pytest.fixture()
def field_username():
    return """#id_username"""
@pytest.fixture()
def field_id_password():
    return """#id_password"""
@pytest.fixture()
def btn_enter():
    return """/html/body/main/main/div[2]/div[2]/form/div[3]/input"""
@pytest.fixture()
def successful_entrance():
    return """/html/body/main/div/div/div/div[2]/div/form/div/div[1]/div[1]/label"""
@pytest.fixture()
def text_unsuccessful_save():
    return """/html/body/main/main/div[2]"""
@pytest.fixture()
def get_alert(self):
    logging.info("Set alert text")
    text = self.get_alert_text()
    logging.info(text)
    return text
@pytest.fixture()
def text_required_field2():
    return """/html/body/main/main/div[2]/div[2]/form/div[4]"""
@pytest.fixture()
def text_required_field1():
    return """/html/body/main/main/div[2]/div[2]/form/div[2]"""
@pytest.fixture()
def text_similar_name():
    return """/html/body/main/main/div[2]/div[2]/form/div[4]"""
@pytest.fixture()
def text_short_pass():
    return """/html/body/main/main/div[2]/div[2]/form/div[5]"""
@pytest.fixture()
def text_not_match():
    return """/html/body/main/main/div[2]/div[2]/form/p"""

# бонусные проверки
@pytest.fixture()
def btn_search():
    return """//*[@id="search"]"""
@pytest.fixture()
def btn_megano_emage():
    return """/html/body/header/header/div[2]/div/div[1]/a/img"""
@pytest.fixture()
def text_navigation():
    return """/html/body/footer/footer/div/div/div[2]/strong"""
