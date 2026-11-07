from playwright.sync_api import Page


class Item():

    def __init__(self,page:Page):

        self.page=page


        self.item1=page.locator("#add-to-cart-sauce-labs-backpack")
        self.item2=page.locator("#add-to-cart-sauce-labs-bike-light")
        self.item3=page.locator("#add-to-cart-sauce-labs-bolt-t-shirt")


    def item_click(self):

        self.item1.click()
        self.item2.click()
        self.item3.click()








        