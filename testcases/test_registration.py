"""here we can run registration page"""
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path="D:\Browserdriver\chromedriver.exe")
driver.get("https://nextv3.elemetrik.net/elemetrik-registration/signup/registration")
driver.find_element_by_name("firstName").click()
driver.find_element_by_name("firstName").clear()
driver.find_element_by_name("firstName").send_keys("Rabi")
driver.find_element_by_name("lastName").click()
driver.find_element_by_name("lastName").clear()
driver.find_element_by_name("lastName").send_keys("Behera")
driver.find_element_by_name("email").click()
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("rabinarayanbehera00@gmail.com")
driver.find_element_by_name("name").click()
driver.find_element_by_name("name").clear()
driver.find_element_by_name("name").send_keys("rabi")
driver.find_element_by_name("siteDomain").click()
driver.find_element_by_name("siteDomain").clear()
driver.find_element_by_name("siteDomain").send_keys("rabi")
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Which modules are you most interested in ?'])[1]/following::*[name()='svg'][1]").click()
driver.find_element_by_xpath("//div[@id='react-select-2-option-1']").click()
driver.find_element_by_xpath("//div[@id='main-wrapper']/div/div/div/div/div[2]/div/div[2]/div[2]/div[6]/button/span").click()

