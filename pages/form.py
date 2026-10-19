from playwright.sync_api import Page


class Form:

    def __init__(self, page: Page):
        self.page = page

        self.firstname = page.get_by_placeholder('First Name')
        self.lastname = page.get_by_placeholder('Last Name')
        self.email = page.get_by_placeholder('name@example.com')
        self.mobile = page.get_by_placeholder('Mobile Number')
        self.subject = page.locator('#subjectsInput')
        self.gender=page.get_by_text("Male",exact=True)
        self.hobby=page.get_by_text("Sports",exact=True)

        self.butten=page.locator('#submit')




    def open(self):
        self.page.goto("https://demoqa.com/automation-practice-form")


    def name(self, first, last):
        self.firstname.fill(first)
        self.lastname.fill(last)

    def email_fild(self, gmail):
        self.email.fill(gmail)

    def mobile_fild(self, m):
        self.mobile.fill(m)


    def state(self):
        self.page.get_by_text("Select State", exact=True).click()

        self.page.get_by_text("NCR",exact=True).click()



    def city(self):
        self.page.get_by_text("Select City", exact=True).click()

        self.page.get_by_text("Jaipur", exact=True).click()

