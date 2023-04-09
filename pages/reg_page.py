from .base_page import BasePage
from .locators import BaseLocators, RegPageLocators, EmailConfirmPageLocators, UserAgreementPageLocators


class RegPage(BasePage):
    # T21 Проверка местоположения поля ввода имени, кнопки "Зарегистрироваться", ссылки на пользовательское соглашение
    def location_of_input_fields_and_buttons_and_links(self):
        assert self.is_element_present(RegPageLocators.REG_FIRST_NAME_INPUT_PAGE_RIGHT), "element not found"
        assert self.is_element_present(RegPageLocators.REG_REGISTER_BUTTON_PAGE_RIGHT), "element not found"
        assert self.is_element_present(RegPageLocators.REG_USER_AGREEMENT_LINK_PAGE_RIGHT), "element not found"

    # T22 Валидация поля ввода (ввод валидных данных: имя)
    def text_field_validation_valid_data(self, input_text):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_not_element_present(RegPageLocators.REG_ERROR_FIRST_NAME_INPUT), "element found"

    # T23 Валидация поля ввода (ввод валидных данных: email или номер мобильного телефона)
    def email_or_phone_field_validation_valid_data(self, input_text):
        self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        element = self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT_VALUE)
        value = element.get_attribute("value")
        assert input_text == value, "email or phone do not match"
        assert self.is_not_element_present(RegPageLocators.REG_ERROR_INVALID_EMAIL_OR_PHONE_INPUT), "element found"

    # T24 Валидация поля ввода (ввод валидных данных: пароль)
    def password_field_validation_valid_data(self, input_text):
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_not_element_present(RegPageLocators.REG_ERROR_INVALID_PASSWORD_INPUT), "element found"

    # T25 Регистрация с помощью валидных данных
    def registration_with_valid_data(self, first_name, last_name, email_phone, password):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(RegPageLocators.REG_LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(email_phone)
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_ENTER_BUTTON).click()
        assert self.is_element_present(EmailConfirmPageLocators.EMAIL_CONF_HEADING), "element not found"

    # T26 Переход на страницу с пользовательским соглашением (ссылка под кнопкой "Зарегистрироваться")
    def link_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(RegPageLocators.REG_USER_AGREEMENT_LINK).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # T27 Переход на страницу с пользовательским соглашением (ссылка в footer)
    def link_fut_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(RegPageLocators.REG_PRIVACY_POLICY_LINK).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # T28 Валидация поля ввода (ввод невалидных данных: имя)
    def text_field_validation_invalid_data(self, input_text):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(RegPageLocators.REG_ERROR_FIRST_NAME_INPUT), "element not found"

    # T29 Валидация поля ввода (ввод невалидных данных: email или номер мобильного телефона)
    def email_or_phone_field_validation_invalid_data(self, input_text):
        self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(RegPageLocators.REG_ERROR_INVALID_EMAIL_OR_PHONE_INPUT), "element not found"

    # T30 Валидация поля ввода (ввод невалидных данных: пароль)
    def password_field_validation_invalid_data(self, input_text):
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(RegPageLocators.REG_ERROR_INVALID_PASSWORD_INPUT), "element not found"

    # T31 Валидация поля ввода (ввод в поле подтверждения пароля данных, отличных от введенных в поле ввода пароля
    def entering_data_in_the_password_confirmation_field(self, password1, password2):
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(password1)
        self.find_element(RegPageLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(password2)
        self.find_element(RegPageLocators.REG_ENTER_BUTTON).click()
        assert self.is_element_present(RegPageLocators.REG_ERROR_PASSWORD_DONT_MATCH), "element not found"

    # T32 Регистрация с помощью невалидных данных
    def registration_with_invalid_data(self, first_name, last_name, email_phone, password):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(RegPageLocators.REG_LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(email_phone)
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_ENTER_BUTTON).click()
        assert self.is_not_element_present(EmailConfirmPageLocators.EMAIL_CONF_HEADING), "element found"