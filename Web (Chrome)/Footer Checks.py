import sys
import time
from time import gmtime, strftime
import datetime
import conf as conf
import self as self
now = datetime.datetime.now()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
options = Options()
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
testurl = 'https://uktv:wemakegreattv@uktvplay.uatuktv.co.uk/'
a = ActionChains(driver)
driver.get(testurl)
driver.implicitly_wait(10)

# Cookie Notice
CookieYes = driver.find_element_by_id('cookie-agree')
CookieYes.click()

time.sleep(2)

# -- Scroll Page --
ScrollPage = driver.find_element_by_tag_name('body')
ScrollPage.send_keys(Keys.END)

# -- Footer --
logofooter = driver.find_element_by_xpath('//*[@id="app"]/footer/div/div[1]/a/img')

help = driver.find_element_by_id('footer-help')
print(help.get_attribute('href'))
TVregistration = driver.find_element_by_id('footer-TVreg')
print(TVregistration.get_attribute('href'))
ContactUs = driver.find_element_by_id('footer-contact')
print(ContactUs.get_attribute('href'))
ParentalGuidance = driver.find_element_by_id('footer-PIN')
print(ParentalGuidance.get_attribute('href'))
WaystoWatch = driver.find_element_by_id('footer-ways')
print(WaystoWatch.get_attribute('href'))

# -- General --

PrivacyPolicy = driver.find_element_by_id('footer-privacy')
print(PrivacyPolicy.get_attribute('href'))
TandC = driver.find_element_by_id('footer-terms')
print(TandC.get_attribute('href'))
Accessibility = driver.find_element_by_id('footer-accessibility')
print(Accessibility.get_attribute('href'))
CookieFooter = driver.find_element_by_id('footer-cookie')
print(CookieFooter.get_attribute('href'))
Corp = driver.find_element_by_id('footer-corporate')
print(Corp.get_attribute('href'))
Footerchannels = driver.find_element_by_id('footer-channels')
print(Footerchannels.get_attribute('href'))
Slavery = driver.find_element_by_id('footer-slavery')
print(Slavery.get_attribute('href'))

# -- Social Feeds Links --

Twitter = driver.find_element_by_id('footer-twitter')
print(Twitter.get_attribute('href'))
Facebook = driver.find_element_by_id('footer-facebook')
print(Facebook.get_attribute('href'))
Instagram = driver.find_element_by_id('footer-instagram')
print(Instagram.get_attribute('href'))

print('Footer Passed')