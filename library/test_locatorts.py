from selenium.webdriver.common.by import By

firstname=(By.NAME,"firstName")
lastname=(By.NAME,"lastName")
email=(By.NAME,"email")
title=(By.NAME,"name")
site_domain=(By.NAME,"siteDomain")
dropdown =(By.XPATH,".//*[normalize-space(text()) and normalize-space(.)='Which modules are you most interested in ?'])[1]/following::*[name()='svg'][1]")
select_0=(By.XPATH,"//div[@id='react-select-2-option-0']")
select_1=(By.XPATH,"//div[@id='react-select-2-option-1']")
select_2=(By.XPATH,"//div[@id='react-select-2-option-2']")
select_3=(By.XPATH,"//div[@id='react-select-2-option-3']")
next =(By.XPATH,"//div[@id='main-wrapper']/div/div/div/div/div[2]/div/div[2]/div[2]/div[6]/button/span")

