# 'https://techstarspace.engineer/2020/02/19/setup-chrome-driver-for-selenium-on-kali-linux/'
# website to help download, setup and start browser
# get linkedin_profile_name_position_company + linkedin_urls from google search results

# everything is working except for the profile data, is not being pulled out/url

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


import pandas as pd
chrome_options = Options()
# chrome_options = ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--lang=en')


# Set the locale
chrome_locale = 'locale-of-choice'
chrome_options.add_argument("--lang={}".format(chrome_locale))
# End - Set the locale

# chrome_options.add_argument('--lang=es')
browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)

sample_profile_page = 'https://my.linkedin.com/in/faizal-hamzam-ahmad-028a90157'
browser.get(sample_profile_page)