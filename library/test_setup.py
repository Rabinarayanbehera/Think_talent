from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path="D:\Browserdriver\chromedriver.exe")
driver.get("https://nextv3.elemetrik.net/elemetrik-registration/signup/registration")
driver.maximize_window()