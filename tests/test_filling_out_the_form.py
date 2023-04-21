from selene import browser, have, be
import os


def test_filling_out_the_form():
    browser.open_url('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Larisa')
    browser.element('#lastName').type('Badmaeva')
    browser.element('#userEmail').type('larilotus12@gmail.com')
    browser.element('[value="Female"]').double_click()
    browser.element('#userNumber').type('8902208866')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element('[value="6"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('[value="1991"]').click()
    browser.element('.react-datepicker__day--012').click()

    browser.element('#subjectsInput').type('Maths').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').send_keys(os.getcwd() + "/resources/IMG_4499.jpg")

    browser.element('#currentAddress').type('Moscow')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Larisa Badmaeva', 'Student Email larilotus12@gmail.com', 'Gender Female',
        'Mobile 8902208866', 'Date of Birth 12 July,1991', 'Subjects Maths', 'Hobbies Sports',
        'Picture IMG_4499.jpg', 'Address Moscow', 'State and City NCR Delhi'))