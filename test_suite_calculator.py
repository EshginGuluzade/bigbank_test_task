import os
os.system('pip install -r requirements.txt')
import time
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from utilities.url_split import page_url
from utilities.inputs import put_amount_value
from utilities.inputs import put_period_value


class TestSuiteCalculator(BaseClass):

    def test_min_amount_boundary_value_TC_LA_004(self):
        log = self.getLogger()
        log.info("Test starting...")
        min_boundary_value = "10 000"
        test_value = "9999"
        self.driver.find_element(By.CLASS_NAME, "bb-edit-amount__content").click()
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        log.info(f"Entering the test value {test_value}")
        put_amount_value(index=input_list[0], test_value=test_value)
        returned_value = input_list[0].get_attribute("value").replace(u'\xa0', u' ')
        log.info(f"The value returned by entering the test value ({test_value}) is {returned_value}")
        assert returned_value == min_boundary_value, 'When the user enters a value which is less than 10000, ' \
                                           'the calculator should display 10000.'

    def test_max_amount_boundary_value_TC_LA_005(self):
        log = self.getLogger()
        max_boundary_value = "250 000"
        test_value = "250001"
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        log.info(f"Entering the test value {test_value}")
        put_amount_value(index=input_list[0], test_value=test_value)
        returned_value = input_list[0].get_attribute("value").replace(u'\xa0', u' ')
        log.info(f"The value returned by entering the test value ({test_value}) is {returned_value}")
        assert returned_value == max_boundary_value, 'When the user enters a value which is greater than 250000, ' \
                                           'the calculator should display 250000.'

    def test_any_amount_TC_LA_006(self):
        log = self.getLogger()
        test_value = "123 456"
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        log.info(f"Entering the test value {test_value}")
        put_amount_value(index=input_list[0], test_value=test_value)
        returned_value = input_list[0].get_attribute("value").replace(u'\xa0', u' ')
        log.info(f"The value returned by entering the test value ({test_value}) is {returned_value}")
        assert returned_value == test_value, 'The value'

    def test_min_period_boundary_value_TC_LP_004(self):
        log = self.getLogger()
        min_boundary_value = "12"
        test_value = "11"
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        put_period_value(index=input_list[1], test_value=test_value)
        log.info(f"Entering the test value {test_value}")
        returned_value = input_list[1].get_attribute("value")
        log.info(f"The value returned by entering the test value ({test_value}) is {returned_value}")
        assert returned_value == min_boundary_value, 'When the user enters a value which is less than 12, ' \
                                           'the calculator should display 12.'

    def test_max_period_boundary_value_TC_LP_005(self):
        log = self.getLogger()
        max_boundary_value = "144"
        test_value = "145"
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        put_period_value(index=input_list[1], test_value=test_value)
        log.info(f"Entering the test value {test_value}")
        returned_value = input_list[1].get_attribute("value")
        log.info(f"The value returned by entering the test value ({test_value}) is {returned_value}")
        assert returned_value == max_boundary_value, 'When the user enters a value which is greater than 144, ' \
                                           'the calculator should display 144.'

    def test_any_period_TC_LP_006(self):
        log = self.getLogger()
        test_value = "72"
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        put_period_value(index=input_list[1], test_value=test_value)
        log.info(f"Entering the test value {test_value}")
        returned_value = input_list[1].get_attribute("value")
        log.info(f"The value returned by entering the test value ({test_value}) is {returned_value}")
        assert returned_value == test_value, 'When the user enters a value which is less than 12, ' \
                                           'the calculator should display 12.'

    def test_monthly_payment_less_than_default_amount_TC_MP_001(self):
        log = self.getLogger()
        loan_amount = "84000"
        default_result = self.driver.find_element(By.CLASS_NAME, "bb-calculator__result-value").text
        log.info(f"Default monthly payment is {default_result}")
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        put_amount_value(index=input_list[0], test_value=loan_amount)
        log.info(f"Entering the test value {loan_amount}")
        time.sleep(0.5)
        final_result = self.driver.find_element(By.CLASS_NAME, "bb-calculator__result-value").text
        log.info(f"New monthly payment is {final_result}")
        assert final_result != default_result, 'The monthly payment should be changed'

    def test_monthly_payment_more_than_default_amount_TC_MP_002(self):
        log = self.getLogger()
        loan_amount = "86000"
        default_result = self.driver.find_element(By.CLASS_NAME, "bb-calculator__result-value").text
        log.info(f"Default monthly payment is {default_result}")
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        put_amount_value(index=input_list[0], test_value=loan_amount)
        log.info(f"Entering the test value {loan_amount}")
        time.sleep(0.5)
        final_result = self.driver.find_element(By.CLASS_NAME, "bb-calculator__result-value").text
        log.info(f"New monthly payment is {final_result}")
        assert final_result != default_result, 'The monthly payment should be changed'

    def test_monthly_payment_less_than_default_period_TC_MP_003(self):
        log = self.getLogger()
        loan_period = "110"
        default_result = self.driver.find_element(By.CLASS_NAME, "bb-calculator__result-value").text
        log.info(f"Default monthly payment is {default_result}")
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        log.info(f"Entering the test value {loan_period}")
        put_period_value(index=input_list[1], test_value=loan_period)
        time.sleep(0.5)
        final_result = self.driver.find_element(By.CLASS_NAME, "bb-calculator__result-value").text
        log.info(f"New monthly payment is {final_result}")
        assert final_result != default_result, 'The monthly payment should be changed'

    def test_monthly_payment_more_than_default_period_TC_MP_004(self):
        log = self.getLogger()
        loan_period = "130"
        default_result = self.driver.find_element(By.CLASS_NAME, "bb-calculator__result-value").text
        log.info(f"Default monthly payment is {default_result}")
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        log.info(f"Entering the test value {loan_period}")
        put_period_value(index=input_list[1], test_value=loan_period)
        time.sleep(0.5)
        final_result = self.driver.find_element(By.CLASS_NAME, "bb-calculator__result-value").text
        log.info(f"New monthly payment is {final_result}")
        assert final_result != default_result, 'The monthly payment should be changed'

    def test_interest_rate_less_than_default_amount_TC_IR_001(self):
        log = self.getLogger()
        loan_amount = "84000"
        default_result = self.driver.find_element(By.CLASS_NAME, "bb-list-item__default-slot").text
        log.info(f"Default interest rate is {default_result}")
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        put_amount_value(index=input_list[0], test_value=loan_amount)
        log.info(f"Entering the test value {loan_amount}")
        time.sleep(0.5)
        final_result = self.driver.find_element(By.CLASS_NAME, "bb-list-item__default-slot").text
        log.info(f"New interest rate is {final_result}")
        assert final_result != default_result, 'The interest rate should be changed'

    def test_interest_rate_more_than_default_amount_TC_IR_002(self):
        log = self.getLogger()
        loan_amount = "86000"
        default_result = self.driver.find_element(By.CLASS_NAME, "bb-list-item__default-slot").text
        log.info(f"Default interest rate is {default_result}")
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        put_amount_value(index=input_list[0], test_value=loan_amount)
        log.info(f"Entering the test value {loan_amount}")
        time.sleep(0.5)
        final_result = self.driver.find_element(By.CLASS_NAME, "bb-list-item__default-slot").text
        log.info(f"New interest rate is {final_result}")
        assert final_result != default_result, 'The interest rate should be changed'

    def test_interest_rate_less_than_default_period_TC_IR_003(self):
        log = self.getLogger()
        loan_period = "110"
        default_result = self.driver.find_element(By.CLASS_NAME, "bb-list-item__default-slot").text
        log.info(f"Default interest rate is {default_result}")
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        log.info(f"Entering the test value {loan_period}")
        put_period_value(index=input_list[1], test_value=loan_period)
        time.sleep(0.5)
        final_result = self.driver.find_element(By.CLASS_NAME, "bb-list-item__default-slot").text
        log.info(f"New interest rate is {final_result}")
        assert final_result != default_result, 'The interest rate should be changed'

    def test_interest_rate_more_than_default_period_TC_IR_004(self):
        log = self.getLogger()
        loan_period = "130"
        default_result = self.driver.find_element(By.CLASS_NAME, "bb-list-item__default-slot").text
        log.info(f"Default interest rate is {default_result}")
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        log.info(f"Entering the test value {loan_period}")
        put_period_value(index=input_list[1], test_value=loan_period)
        time.sleep(0.5)
        final_result = self.driver.find_element(By.CLASS_NAME, "bb-list-item__default-slot").text
        log.info(f"New interest rate is {final_result}")
        assert final_result != default_result, 'The interest rate should be changed'

    def test_save_button_without_clicking_TC_SB_001(self):
        log = self.getLogger()
        loan_amount = "34580"
        loan_period = "36"
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        log.info(f"Entering the loan amount test value {loan_amount}")
        put_amount_value(index=input_list[0], test_value=loan_amount)
        log.info(f"Entering the loan period test value {loan_period}")
        put_period_value(index=input_list[1], test_value=loan_period)

        self.driver.find_element(By.CSS_SELECTOR, "path[class='svg2492519115__a bb-icon__dynamic-fill']").click()
        url = self.driver.current_url
        amount = page_url(0, url)
        log.info(f"API endpoint: amount= {amount}")
        period = page_url(1, url)
        log.info(f"API endpoint: period= {period}")
        interest = page_url(2, url)
        log.info(f"API endpoint: InterestRate= {interest}")

        assert amount == "85000", 'Query amount should be 85000'
        assert period == "120", 'Query period should be 120'
        assert interest == "10.95", 'Query interest rate should be 10.95'

    def test_save_button_by_clicking_TC_SB_002(self):
        log = self.getLogger()
        loan_amount = "25000"
        loan_period = "48"
        self.driver.find_element(By.CLASS_NAME, "bb-edit-amount__content").click()
        input_list = self.driver.find_elements(By.CLASS_NAME, "bb-currency-input__input")
        log.info(f"Entering the loan amount test value {loan_amount}")
        put_amount_value(index=input_list[0], test_value=loan_amount)
        log.info(f"Entering the loan period test value {loan_period}")
        put_period_value(index=input_list[1], test_value=loan_period)

        self.driver.find_element(By.CSS_SELECTOR, "button[class='bb-calculator-modal__submit-button bb-button "
                                                  "bb-button--label bb-button--mint bb-button--md bb-button--block']").click()
        url = self.driver.current_url
        amount = page_url(0, url)
        log.info(f"API endpoint: amount= {amount}")
        period = page_url(1, url)
        log.info(f"API endpoint: period= {period}")
        interest = page_url(2, url)
        log.info(f"API endpoint: InterestRate= {interest}")

        assert amount != "85000", 'API "amount" query should be changed'
        assert period != "120", 'API "period" query should be changed'
        assert interest != "10.95", 'API "InterestRate" query should be changed'
