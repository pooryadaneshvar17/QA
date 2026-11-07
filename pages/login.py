from playwright.sync_api import Page


class Login():

    def __init__(self, page:Page):


        self.page=page

        self.login_btn= page.locator("#login-button")    

        self.login_e=page.locator('[aria-label="Dismiss error"]')

        self.username=page.locator('#user-name')
        self.password=page.locator('#password')



    def open_site(self):

        self.page.goto("https://www.saucedemo.com/")   





    def user(self,username,pas):

        self.username.fill(username)
        self.password.fill(pas)
