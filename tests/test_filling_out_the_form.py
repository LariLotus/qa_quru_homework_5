from selene import browser, have, be
import os


def test_filling_out_the_form():
    browser.open_url('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Larisa')
    browser.element('#lastName').type('Badmaeva')
    browser.element('#userEmail').type('larilotus12@gmail.com')
    browser.element('[value="Female"]').double_click()
    browser.element('#userNumber').type('89022088667')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element('[value="6"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('[value="1991"]').click()
    browser.element('.react-datepicker__day--012').click()

    browser.element('#subjectsInput').type('Math').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').send_keys(os.getcwd()+"/tests/resources/IMG_4499.jpg")

    browser.element('[id=currentAddress]').type('Moscow')
    # browser.element('#state').click()
    # browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Rajasthan')).click()
    browser.element('[id=react-select-3-input]').type('NCR').press_enter()
    # browser.element('#city').click()
    browser.element('[id=react-select-4-input]').type('Delhi').press_enter()


    browser.element('#submit').press_enter()

    browser.all('#userForm').element_by(have.exact_text(
        'Student name Larisa Badmaeva', 'student Email larilotus12@gmail.com', 'Gender Female', 'Mobile 89022088667',
        'Date of Birth 12 July 1991', 'Subjects Math', 'Hobbies Sports', 'Picture IMG_4499.jpg',
        'Current Address Moscow', 'State and City NCR Delhi'))