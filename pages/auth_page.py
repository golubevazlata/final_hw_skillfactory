from settings import valid_email, sql_injection, random_int
from .base_page import BasePage
from .locators import BaseLocators, AuthPageLocators, ChangePassPageLocators, RegPageLocators, \
    UserAgreementPageLocators, RejectedRequestPageLocators


class AuthPage(BasePage):
    # T1 Открытие формы авторизации
    def the_authorization_form_is_open(self):
        assert self.is_element_present(AuthPageLocators.AUTH_HEADING)
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth" in self.browser.current_url, \
            "url do not match"

    # T2 Местоположение продуктового слогана и логотипа ЛК "Ростелеком ID"
    def location_of_the_logo_and_slogan(self):
        assert self.is_element_present(AuthPageLocators.AUTH_LOGO), "element not found"
        assert self.is_element_present(AuthPageLocators.AUTH_SLOGAN), "element not found"

    # T3 Местоположение меню выбора типа аутентификации
    def location_of_the_tab_menu(self):
        assert self.is_element_present(AuthPageLocators.AUTH_TAB_MENU), "element not found"

    # T4 Проверка типа аутентификации по умолчанию
    def default_authentication_type(self):
        assert self.is_element_present(AuthPageLocators.AUTH_USERNAME_INPUT_PLACEHOLDER_TELEPHONE), \
            "element not found"

    # T5 Автоматическое изменение типа аутентификации
    def automatic_change_of_authentication_type(self):
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(valid_email())
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(AuthPageLocators.AUTH_USERNAME_INPUT_ACTIV_EMAIL), "element not found"

    # T6 Переход на форму восстановления пароля
    def link_to_the_password_recovery_form(self):
        self.find_element(AuthPageLocators.AUTH_FORGOT_PASSWORD_LINK).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.browser.current_url, "url do not match"
        assert self.is_element_present(ChangePassPageLocators.CHANGE_PASS_HEADING), "element not found"

    # T7 Переход на форму регистрации
    def link_to_the_registration_form(self):
        self.find_element(AuthPageLocators.AUTH_REGISTER_LINK).click()
        assert self.is_element_present(RegPageLocators.REG_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration" \
               in self.browser.current_url, "url do not match"

    # T8 Переход на страницу с пользовательским соглашением (ссылка под кнопкой "Войти")
    def link_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(AuthPageLocators.AUTH_USER_AGREEMENT_LINK).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # T9 Переход на страницу с пользовательским соглашением (ссылка расположена в footer)
    def link_fut_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(AuthPageLocators.AUTH_PRIVACY_POLICY_LINK).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # T10 Переход по ссылке на страницу авторизации с помощью соцсети "ВКонтакте"
    def link_to_social_vk(self):
        self.find_element(AuthPageLocators.AUTH_SOCIAL_VK_LINK).click()
        assert "https://oauth.vk.com/authorize" in self.browser.current_url, "url do not match"

    # T11 Попытка авторизации с незаполненными полями ввода данных
    def authorization_with_blank_fields(self):
        self.find_element(AuthPageLocators.AUTH_TAB_PHONE).click()
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert self.is_element_present(AuthPageLocators.AUTH_ERROR_ENTER_PHONE_NUMBER), "element not found"
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth" in self.browser.current_url, \
            "url do not match"

    # T12 Проверка на безопасность ввода данных в текстовое поле (уязвимость)
    def sql_injection_in_a_text_field(self):
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(sql_injection())
        self.find_element(AuthPageLocators.AUTH_PASSWORD_INPUT).send_keys(random_int())
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert self.is_element_present(RejectedRequestPageLocators.REJECTED_REQUEST_HEADING), "element not found"
        assert self.is_element_present(RejectedRequestPageLocators.REJECTED_REQUEST_INFO), "element not found"
