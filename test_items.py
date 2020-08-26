link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_user_should_see_button_add_to_basket(browser):
    browser.get(link)
    # time.sleep(30)  # it needs to test button text
    basket_button = browser.find_elements_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(basket_button) > 0, "Button here!"

