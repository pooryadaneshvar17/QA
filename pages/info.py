from playwright.sync_api import Page

class Info():

    def __init__(self,page:Page):

        self.page=page


        self.next=page.locator("#continue")

        self.next_e=page.locator('[aria-label="Dismiss error"]')

        self.first=page.locator("#first-name")
        self.last=page.locator("#last-name")
        self.postal=page.locator("#postal-code")

        self.total=page.locator('[data-test="total-label"]')

        self.finish=page.locator("#finish")

        self.messag=page.get_by_text("Thank you for your order!",exact=True)

        self.home=page.locator("#back-to-products")






    def information(self,firstname,lastname,code):

        self.first.fill(firstname)
        self.last.fill(lastname)
        self.postal.fill(code)  

        