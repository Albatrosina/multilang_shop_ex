import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_btn_is_displayed(browser):
    browser.get(link)
    basket_btn = browser.find_element_by_css_selector("#add_to_basket_form > button")
    assert basket_btn.is_displayed()
    time.sleep(10)