from library.test_setup import *
from library.test_locatorts import *

# driver.find_element(firstname).click()
# driver.find_element(firstname).clear()
driver.find_element(firstname).send_keys("Rabi")
# driver.find_element(lastname).click()
# driver.find_element(lastname).clear()
driver.find_element(lastname).send_keys("Behera")
# driver.find_element(email).click()
# driver.find_element(email).clear()
driver.find_element(email).send_keys("rabinarayanbehera00@gmail.com")
# driver.find_element(title).click()
# driver.find_element(title).clear()
driver.find_element(title).send_keys("rabi")
# driver.find_element(site_domain).click()
# driver.find_element(site_domain).clear()
driver.find_element(site_domain).send_keys("rabi")
driver.find_element(dropdown).click()
driver.find_element(select_1).click()
driver.find_element(next).click()