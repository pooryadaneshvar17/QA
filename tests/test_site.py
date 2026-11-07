from playwright.sync_api import expect,Page

from pages.login import Login
from pages.item import Item
from pages.cart import Cart
from pages.info import Info 




def test_login(page):

    login=Login(page)
    item=Item(page)
    cart=Cart(page)
    info=Info(page)


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

    cart.check.click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")


    info.next.click()

    expect(info.next_e).to_be_visible()

    info.information("Poorya","Aria","17")

    info.next.click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    expect(info.total).to_be_visible()

    info.finish.click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    expect(info.messag).to_be_visible()
    expect(info.messag).to_contain_text("Thank you for your order!")


    info.home.click()













    


    




    page.pause()

    
