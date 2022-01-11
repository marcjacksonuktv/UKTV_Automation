import sys
import time
from time import gmtime, strftime
import datetime
import conf as conf
import self as self
now = datetime.datetime.now()
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.opera import OperaDriverManager
driver = webdriver.Opera(executable_path=OperaDriverManager().install())
testurl = 'https://uktv:wemakegreattv@uktvplay.uatuktv.co.uk/'
driver.set_window_size(500, 1000)
a = ActionChains(driver)
driver.get(testurl)
driver.implicitly_wait(10)

# Cookie Notice
CookieYes = driver.find_element_by_id('cookie-agree').click()
time.sleep(2)

# Burger Menu
BurgerMenu = driver.find_element_by_id('mobile-nav-menu').click()
time.sleep(2)

# My Account Register
MyAccount = driver.find_element_by_id('side-nav-account')
MyAccount.click()
time.sleep(2)
RegistertoWatch = driver.find_element_by_id('register-now-link')
RegistertoWatch.click()
time.sleep(2)

# Register Form
email = driver.find_element_by_id('emailAddress').send_keys('operausermob@testaccount.com')
password = driver.find_element_by_id('password').send_keys('password123')

FirstName = driver.find_element_by_id('firstName').send_keys('Gurjeet')
LastName = driver.find_element_by_id('lastName').send_keys('Kaur')

DateofBirt_Day = driver.find_element_by_id('registration_DateOfBirth_Day').send_keys('1')
DateofBirt_Month = driver.find_element_by_id('registration_DateOfBirth_Month').send_keys('1')
DateofBirt_Year = driver.find_element_by_id('registration_DateOfBirth_Year').send_keys('1995')

Gender = driver.find_element_by_id('gender').send_keys('Female')
Postcode = driver.find_element_by_id('postCode').send_keys('W6 7AP')

News_opt_in = driver.find_element_by_id('subscribeNewsletter').click()

Registertowatch_button = driver.find_element_by_id('register-btn').click()
time.sleep(5)
RegisterationComplete_Continuebutton = driver.find_element_by_class_name('submit-button').click()