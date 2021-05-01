# SangTengkorak
# May 01 2021

from selenium import webdriver

typed_in = input("What you want to search in youtube? ")

# https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver

driver = webdriver.Chrome()
driver.get('https://youtube.com')
searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys(f"{typed_in}")

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()
