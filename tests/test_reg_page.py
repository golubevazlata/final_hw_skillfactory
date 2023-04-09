# python -m pytest -v --tb=line tests/test_reg_page.py

import pytest
from pages.reg_page import RegPage
from settings import url_base_page, invalid_name, valid_email_or_phone, valid_password, valid_first_name, \
    valid_last_name, invalid_email_or_phone, invalid_password, valid_password2, random_int, first_name_en, \
    chinese_chars, russian_chars


class TestRegPage():
    def test_T21_location_of_input_fields_and_buttons_and_links(self, browser):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.location_of_input_fields_and_buttons_and_links()

    @pytest.mark.parametrize('input_text', valid_first_name)
    def test_T22_text_field_validation_valid_data(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.text_field_validation_valid_data(input_text)

    @pytest.mark.parametrize('input_text', valid_email_or_phone)
    def test_T23_email_or_phone_field_validation_valid_data(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.email_or_phone_field_validation_valid_data(input_text)

    @pytest.mark.parametrize('input_text', valid_password)
    def test_T24_password_field_validation_valid_data(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.password_field_validation_valid_data(input_text)

    @pytest.mark.parametrize('first_name', valid_first_name)
    @pytest.mark.parametrize('last_name', valid_last_name)
    @pytest.mark.parametrize('email_phone', valid_email_or_phone)
    @pytest.mark.parametrize('password', valid_password)
    def test_T25_registration_with_valid_data(self, browser, first_name, last_name, email_phone, password):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.registration_with_valid_data(first_name, last_name, email_phone, password)

    def test_T26_link_to_the_user_agreement_page(self, browser):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.link_to_the_user_agreement_page()

    def test_T27_link_fut_to_the_user_agreement_page(self, browser):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.link_fut_to_the_user_agreement_page()

    @pytest.mark.parametrize('input_text', invalid_name)
    def test_T28_text_field_validation_invalid_data(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.text_field_validation_invalid_data(input_text)

    @pytest.mark.parametrize('input_text', invalid_email_or_phone)
    def test_T29_email_or_phone_field_validation_invalid_data(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.email_or_phone_field_validation_invalid_data(input_text)

    @pytest.mark.parametrize('input_text', invalid_password)
    def test_T30_password_field_validation_invalid_data(self, browser, input_text):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.password_field_validation_invalid_data(input_text)

    @pytest.mark.parametrize('password1', valid_password)
    @pytest.mark.parametrize('password2', valid_password2)
    def test_T31_entering_data_in_the_password_confirmation_field(self, browser, password1, password2):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.entering_data_in_the_password_confirmation_field(password1, password2)

    @pytest.mark.parametrize('first_name', [random_int()])
    @pytest.mark.parametrize('last_name', [first_name_en()])
    @pytest.mark.parametrize('email_phone', [chinese_chars()])
    @pytest.mark.parametrize('password', [russian_chars()])
    def test_T32_registration_with_invalid_data(self, browser, first_name, last_name, email_phone, password):
        reg_page = RegPage(browser, url_base_page)
        reg_page.open_reg_page()
        reg_page.registration_with_invalid_data(first_name, last_name, email_phone, password)