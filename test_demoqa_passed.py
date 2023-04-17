import os.path
from selene import browser, have, be
from selene.support.shared import browser
from selene import command


def test_complete_registration_demoqa():
    browser.config.browser_name = 'Google Chrome'
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.open()
    browser.driver.maximize_window()

    browser.open('/')
    browser.should(have.title("DEMOQA"))

    browser.element('#firstName').send_keys("Albert")
    browser.element('#lastName').send_keys("Ivanov")
    browser.element('#userEmail').send_keys("ALLIIVAN@mail.ru")
    browser.element('#userNumber').send_keys("8954567689")

    browser.element('[name = gender][value = Male]+label').click()

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('December')
    browser.element('.react-datepicker__year-select').send_keys('1993')
    browser.element(f'.react-datepicker__day--0{28}').click()

    browser.element('#subjectsInput').send_keys('Physics').send_keys('Enter')
    browser.all('[for = hobbies-checkbox-1]').element_by(have.exact_text('Sports')).click()
    browser.all('[for = hobbies-checkbox-2]').element_by(have.exact_text('Reading')).click()
    browser.all('[for = hobbies-checkbox-3]').element_by(have.exact_text('Music')).click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('../qa_guru_home_work_5_5/resource/pictures.jpg'))

    browser.element('#currentAddress').perform(command.js.scroll_into_view)
    browser.element('#currentAddress').send_keys('Pharabi street 18')

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Rajasthan')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Jaipur')).click()

    browser.element('#submit').perform(command.js.click)

    # THEN

    # browser.element('.table-responsive').al('td').should(
    #     (Student Name, Albert
    # )




