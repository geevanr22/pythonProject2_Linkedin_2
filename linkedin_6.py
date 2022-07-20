# 'https://techstarspace.engineer/2020/02/19/setup-chrome-driver-for-selenium-on-kali-linux/'
#  website to help download, setup and start browser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


import pandas as pd
chrome_options = Options()
# chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--lang=en')


# Set the locale
chrome_locale = 'locale-of-choice'
chrome_options.add_argument("--lang={}".format(chrome_locale))
# End - Set the locale

chrome_options.add_argument('--lang=es')
browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=Options())

from time import sleep
from selenium.webdriver.common.by import By

company_name = 'petronas'
job_position = 'accounts payable'
pages_to_scrape = 4

search_url_2 = f'https://www.google.com/search?q={company_name}+linkedin+%27{job_position}%27&tbas=0&ei=SB7VYvuADvmI4-' \
               f'EPsqiquAI&start=0&sa=N&ved=2ahUKEwj7xMbqhoL5AhV5xDgGHTKUCic4FBDy0wN6BAgBEDc&biw=1920&bih=793&dpr=1'

browser.get(search_url_2)

page_num_xpath = '//tr[@jsname="TeSSVd"]//td'
page_num_element = browser.find_elements(By.XPATH, page_num_xpath)
page_num_list = []

for num in page_num_element:
    page_num_list.append(num.text) # append to list above

browser.quit()
pages_to_scrape = (page_num_list[-2])




for i in range(0, pages_to_scrape):
    browser.get(f'https://www.google.com/search?q={company_name}+linkedin+{job_position}&rlz=1C1GCEU_enMY1010MY1010&sxsrf=ALiCzsab9e1Jhi9YQj_RwF6dvq42UT_RBA:1658221649255&ei=UXTWYsObD5Ox4-EP2deuyAI&start={i}0&sa=N&ved=2ahUKEwiDiPOCzYT5AhWT2DgGHdmrCykQ8tMDegQIARA5&biw=907&bih=722&dpr=1.2')
    sleep(3)
    i += 1

sleep(5)
browser.quit()