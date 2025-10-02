from ..sd_pages.login_page import LoginPage
from ..sd_pages.chooseproduct import ChoosePage
from ..sd_pages.cart_page import CartPage
import pytest


def way_to_checkout(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")
    add_item = ChoosePage(page)
    add_item.go_to_cart()
    page.wait_for_url("**/cart.html")
    cart_page = CartPage(page)
    cart_page.checkout()


@pytest.mark.parametrize('username, password, expected',[
('standard_user', 'secret_sauce', True ),
('locked_out_user', 'secret_sauce',False  ),
('problem_user', 'secret_sauce', True),
('error_user', 'secret_sauce', True),
('visual_user', 'secret_sauce',True)
                         ])
def test_login(page, username, password, expected):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(username, password)

    if expected:
        assert 'inventory' in page.url
    else:
        assert page.get_by_text("Epic sadface: Sorry, this user has been locked out.").is_visible()
