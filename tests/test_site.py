from playwright.sync_api import expect,Page

from pages.login import Login
from pages.item import Item
from pages.cart import Cart



def test_login(page):

    login=Login(page)
    item=Item(page)
    cart=Cart(page)


    login.open_site()

    login.login_btn.click()
    expect(login.login_e).to_be_visible()

    login.user("standard_user","secret_sauce")

    login.login_btn.click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


    item.item_click()

    item.shoping_cart.click()


    


    expect(page).to_have_url("https://www.saucedemo.com/cart.html")


    cart.ok_item()

    


    




    page.pause()

    
