from ..sd_pages.chooseproduct import ChoosePage
from ..sd_pages.login_page import LoginPage



def test_add_item(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")
    add_item = ChoosePage(page)
    add_item.go_to_cart()
    assert add_item.get_total_quantity() == 2