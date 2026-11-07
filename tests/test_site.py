from playwright.sync_api import expect,Page

from pages.login import Login


def test_login(page):

    login=Login(page)


    login.open_site()

    login.login_btn.click()
    expect(login.login_e).to_be_visible()

    login.user("standard_user","secret_sauce")

    login.login_btn.click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    


    page.pause()

    
