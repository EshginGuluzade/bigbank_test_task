from selenium.webdriver.common.keys import Keys

"""
    This two functions click on the amount or period edit button by taking button index.
    Then delete the default value, enters a new test value and press 'Return'
"""

def put_amount_value(index, test_value):
    index.click()
    index.send_keys(Keys.CONTROL + "a")
    index.send_keys(Keys.COMMAND + "a")
    index.send_keys(Keys.BACK_SPACE)
    index.send_keys(Keys.DELETE)
    index.send_keys(test_value)
    index.send_keys(Keys.RETURN)

def put_period_value(index, test_value):
    index.click()
    index.send_keys(Keys.CONTROL + "a")
    index.send_keys(Keys.COMMAND + "a")
    index.send_keys(Keys.BACK_SPACE)
    index.send_keys(Keys.DELETE)
    index.send_keys(test_value)
    index.send_keys(Keys.RETURN)

