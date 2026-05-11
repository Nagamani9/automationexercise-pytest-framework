from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignupPage(BasePage):

    # =====================================================
    # Signup Section
    # =====================================================

    SIGNUP_NAME_INPUT = (
        By.XPATH,
        "//input[@data-qa='signup-name']"
    )

    SIGNUP_EMAIL_INPUT = (
        By.XPATH,
        "//input[@data-qa='signup-email']"
    )

    SIGNUP_BUTTON = (
        By.XPATH,
        "//button[@data-qa='signup-button']"
    )

    # =====================================================
    # Account Information
    # =====================================================

    ENTER_ACCOUNT_INFORMATION_TEXT = (
        By.XPATH,
        "//b[contains(text(),'Enter Account Information')]"
    )

    TITLE_MR_RADIO = (
        By.ID,
        "id_gender1"
    )

    PASSWORD_INPUT = (
        By.ID,
        "password"
    )

    DAYS_DROPDOWN = (
        By.ID,
        "days"
    )

    MONTHS_DROPDOWN = (
        By.ID,
        "months"
    )

    YEARS_DROPDOWN = (
        By.ID,
        "years"
    )

    NEWSLETTER_CHECKBOX = (
        By.ID,
        "newsletter"
    )

    SPECIAL_OFFERS_CHECKBOX = (
        By.ID,
        "optin"
    )

    # =====================================================
    # Address Information
    # =====================================================

    FIRST_NAME_INPUT = (
        By.ID,
        "first_name"
    )

    LAST_NAME_INPUT = (
        By.ID,
        "last_name"
    )

    COMPANY_INPUT = (
        By.ID,
        "company"
    )

    ADDRESS1_INPUT = (
        By.ID,
        "address1"
    )

    ADDRESS2_INPUT = (
        By.ID,
        "address2"
    )

    COUNTRY_DROPDOWN = (
        By.ID,
        "country"
    )

    STATE_INPUT = (
        By.ID,
        "state"
    )

    CITY_INPUT = (
        By.ID,
        "city"
    )

    ZIPCODE_INPUT = (
        By.ID,
        "zipcode"
    )

    MOBILE_NUMBER_INPUT = (
        By.ID,
        "mobile_number"
    )

    CREATE_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[@data-qa='create-account']"
    )

    # =====================================================
    # Account Created / Deleted
    # =====================================================

    ACCOUNT_CREATED_TEXT = (
        By.XPATH,
        "//b[contains(text(),'Account Created!')]"
    )

    ACCOUNT_DELETED_TEXT = (
        By.XPATH,
        "//b[contains(text(),'Account Deleted!')]"
    )

    CONTINUE_BUTTON = (
        By.XPATH,
        "//a[@data-qa='continue-button']"
    )

    # =====================================================
    # Signup Actions
    # =====================================================

    def enter_signup_name(self, name):

        self.enter_text(
            self.SIGNUP_NAME_INPUT,
            name
        )

    def enter_signup_email(self, email):

        self.enter_text(
            self.SIGNUP_EMAIL_INPUT,
            email
        )

    def click_signup(self):

        self.safe_click(self.SIGNUP_BUTTON)

    # =====================================================
    # Verification Methods
    # =====================================================

    def is_account_information_visible(self):

        return self.is_element_visible(
            self.ENTER_ACCOUNT_INFORMATION_TEXT
        )

    def is_account_created_visible(self):

        return self.is_element_visible(
            self.ACCOUNT_CREATED_TEXT
        )

    def is_account_deleted_visible(self):

        return self.is_element_visible(
            self.ACCOUNT_DELETED_TEXT
        )

    # =====================================================
    # Account Information Actions
    # =====================================================

    def select_title(self):

        self.safe_click(self.TITLE_MR_RADIO)

    def enter_password(self, password):

        self.enter_text(
            self.PASSWORD_INPUT,
            password
        )

    def select_date_of_birth(
            self,
            day,
            month,
            year
    ):

        self.select_dropdown_by_visible_text(
            self.DAYS_DROPDOWN,
            day
        )

        self.select_dropdown_by_visible_text(
            self.MONTHS_DROPDOWN,
            month
        )

        self.select_dropdown_by_visible_text(
            self.YEARS_DROPDOWN,
            year
        )

    def select_newsletter_checkbox(self):
        self.safe_click(
            self.NEWSLETTER_CHECKBOX
        )

    def select_special_offers_checkbox(self):
        self.safe_click(
            self.SPECIAL_OFFERS_CHECKBOX
        )

    # =====================================================
    # Address Actions
    # =====================================================

    def enter_first_name(self, first_name):

        self.enter_text(
            self.FIRST_NAME_INPUT,
            first_name
        )

    def enter_last_name(self, last_name):

        self.enter_text(
            self.LAST_NAME_INPUT,
            last_name
        )

    def enter_company(self, company):

        self.enter_text(
            self.COMPANY_INPUT,
            company
        )

    def enter_address1(self, address1):

        self.enter_text(
            self.ADDRESS1_INPUT,
            address1
        )

    def enter_address2(self, address2):

        self.enter_text(
            self.ADDRESS2_INPUT,
            address2
        )

    def select_country(self, country):

        self.select_dropdown_by_visible_text(
            self.COUNTRY_DROPDOWN,
            country
        )

    def enter_state(self, state):

        self.enter_text(
            self.STATE_INPUT,
            state
        )

    def enter_city(self, city):

        self.enter_text(
            self.CITY_INPUT,
            city
        )

    def enter_zipcode(self, zipcode):

        self.enter_text(
            self.ZIPCODE_INPUT,
            zipcode
        )

    def enter_mobile_number(self, mobile_number):

        self.enter_text(
            self.MOBILE_NUMBER_INPUT,
            mobile_number
        )

    # =====================================================
    # Final Actions
    # =====================================================

    def click_create_account(self):

        self.safe_click(
            self.CREATE_ACCOUNT_BUTTON
        )

    def click_continue(self):

        self.safe_click(
            self.CONTINUE_BUTTON
        )

    # =====================================================
    # Composite Business Flow
    # =====================================================

    def fill_account_information(
            self,
            password,
            day,
            month,
            year,
            first_name,
            last_name,
            company,
            address1,
            address2,
            country,
            state,
            city,
            zipcode,
            mobile_number
    ):

        self.select_title()

        self.enter_password(password)

        self.select_date_of_birth(
            day,
            month,
            year
        )

        self.select_newsletter_checkbox()

        self.select_special_offers_checkbox()

        self.enter_first_name(first_name)

        self.enter_last_name(last_name)

        self.enter_company(company)

        self.enter_address1(address1)

        self.enter_address2(address2)

        self.select_country(country)

        self.enter_state(state)

        self.enter_city(city)

        self.enter_zipcode(zipcode)

        self.enter_mobile_number(mobile_number)