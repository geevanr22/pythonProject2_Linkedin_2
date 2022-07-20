# 'https://techstarspace.engineer/2020/02/19/setup-chrome-driver-for-selenium-on-kali-linux/'
# website to help download, setup and start browser
# this program fetches the number of pages based on the linkedin search url + given parameters

# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# python imports
from time import sleep
import pandas as pd

# chrome webdriver settings
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--lang=en')


# Set the locale
chrome_locale = 'locale-of-choice'
chrome_options.add_argument("--lang={}".format(chrome_locale))

# chrome_options.add_argument('--lang=es')
browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options) # this is what makes all the other add arguments work, or else it just uses
# the initial Options() which is before the add arguments



company_name = 'petronas'
job_position = 'accounts payable'


search_url_2 = f'https://www.google.com/search?q={company_name}+linkedin+%27{job_position}%27&tbas=0&ei=SB7VYvuADvmI4-' \
               f'EPsqiquAI&start=0&sa=N&ved=2ahUKEwj7xMbqhoL5AhV5xDgGHTKUCic4FBDy0wN6BAgBEDc&biw=1920&bih=793&dpr=1'


browser.get(search_url_2)

# here we are trying to get the total number of pages

page_num_xpath = '//tr[@jsname="TeSSVd"]//td'
page_num_element = browser.find_elements(By.XPATH, page_num_xpath)
page_num_list = []

for num in page_num_element:
    page_num_list.append(num.text) # append to list above

print(page_num_list[-2]) # now we can use indexing to get the string of the last page from the page_num_list

sleep(.5)
browser.quit()