from playwright.sync_api import Page


class Form:

    def __init__(self,page:Page):

        self.page=page


        self.firstname=page.get_by_placeholder('First Name')
        self.lastname=page.get_by_placeholder('Last Name')
        self.email=page.get_by_placeholder('name@example.com')





