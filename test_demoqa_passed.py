import os.path
from selene import browser, have
from selene import command
from selene.support.shared import browser


def test_complete_registration_demoqa():
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

    browser.element('#subjectsInput').send_keys('Physics').press_enter()
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

    browser.all('tbody tr').should(have.exact_texts(
        ('Student Name Albert Ivanov',
        'Student Email ALLIIVAN@mail.ru',
        'Gender Male',
        'Mobile 8954567689',
        'Date of Birth 28 November,1993',
        'Subjects Physics',
        'Hobbies Sports, Reading, Music',
        'Picture pictures.jpg',
        'Address Pharabi street 18',
        'State and City Rajasthan Jaipur',)
    ))




