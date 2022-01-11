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
driver.set_window_size(500, 1000)
driver.get(testurl)
driver.implicitly_wait(10)

# Cookie Notice
CookieYes = driver.find_element_by_id('cookie-agree').click()
time.sleep(2)

#Search
Search = driver.find_element_by_id('mobile-nav-search').click()
PopularSearch3 = driver.find_element_by_id('popular-result-1').click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, 700)")
time.sleep(2)

#Continue without Pin
#ContinueWithoutPin = driver.find_element_by_id('continue-pin')
#ContinueWithoutPin.click()
#time.sleep(2)

#Click Episodes on TV Tab
EpsonTV = driver.find_element_by_id('tab-tv').click()
time.sleep(2)
#Click Episodes on Demand Tab
EpsonDemand = driver.find_element_by_id('tab-vod').click()

#Click On Series drop down
SeriesDropdown = driver.find_element_by_xpath('//*[@id="episodes-listings"]/div/section/div/div[1]').click()
time.sleep(2)
#Click On Series1 drop down
Series1 = driver.find_element_by_xpath('//*[@id="episodes-listings"]/div/section/div/div[1]/div[2]/div[1]').click()
SeriesDropdown = driver.find_element_by_xpath('//*[@id="episodes-listings"]/div/section/div/div[1]').click()
time.sleep(2)
#Click On Series2 drop down
Series2 = driver.find_element_by_xpath('//*[@id="episodes-listings"]/div/section/div/div[1]/div[2]/div[2]').click()
SeriesDropdown = driver.find_element_by_xpath('//*[@id="episodes-listings"]/div/section/div/div[1]').click()
time.sleep(2)
#Click On Series3 drop down
Series3 = driver.find_element_by_xpath('//*[@id="episodes-listings"]/div/section/div/div[1]/div[2]/div[3]').click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, 1600)")
time.sleep(2)

#Click Additional episodes
#AdditonalEp1 = driver.find_element_by_id('undefined-1').click()
#time.sleep(2)

#driver.execute_script("window.scrollTo(0, 1500)")
#time.sleep(2)

#AdditonalEp2 = driver.find_element_by_id('undefined-2').click()
#time.sleep(2)

#driver.execute_script("window.scrollTo(0, 1700)")
#time.sleep(2)
#More like this carousel shows