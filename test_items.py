import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_link_button(browser):
    try:
        browser.get(link)
        browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']").click()
    except NoSuchElementException:
        assert False
    assert True
