# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://nextv3.elemetrik.net/elemetrik-registration/signup/registration")
        driver.find_element_by_name("firstName").click()
        driver.find_element_by_name("firstName").clear()
        driver.find_element_by_name("firstName").send_keys("rabu")
        driver.find_element_by_name("lastName").click()
        driver.find_element_by_name("lastName").clear()
        driver.find_element_by_name("lastName").send_keys("jahah")
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("ncscbsgj@email.com")
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("jkcgsgcsh")
        driver.find_element_by_name("siteDomain").click()
        driver.find_element_by_name("siteDomain").clear()
        driver.find_element_by_name("siteDomain").send_keys("scbsjchsk")
        driver.find_element_by_xpath(
            "//div[@id='main-wrapper']/div/div/div/div/div[2]/div/div[2]/div[2]/div[5]/div/div/div/div").click()
        driver.find_element_by_id("react-select-2-option-4").click()
        driver.find_element_by_xpath(
            "//div[@id='main-wrapper']/div/div/div/div/div[2]/div/div[2]/div[2]/div[6]/button/span").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
