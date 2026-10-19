from playwright.sync_api import expect

from pages.form import Form



def test_fill_form(page):
    form=Form(page)

    form.open()

    form.name('poorya','daneshvar')

    form.email_fild('poorya@gmail.com')

    form.gender.click()

    form.mobile_fild('004694930453')


    form.hobby.click()

    form.state()
    form.city()

    form.butten.click()



    page.pause()