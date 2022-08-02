from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd

opt = Options()
opt.add_experimental_option('debuggerAddress', 'localhost:9222')
opt.add_argument('--headless')

browser = webdriver.Chrome(executable_path='chromedriver', options=opt)

# page = 'tao-of-py'
# url = f'https://www.{page}.com'

country = 'Malaysia'
full_url = f'https://www.adipec.com/exhibitorlist?countryName={country}&productCategory&ProductSubcategory&CompanyName&StandNumber'

browser.get(full_url)

# scrolling


page_height = browser.execute_script('return document.body.scrollHeight')
print(f'Print Height: {page_height}')
scrolling_speed = 70


for scroll in range(0, (page_height), scrolling_speed):
    browser.execute_script(f'window.scrollTo(0, {scroll})')
    sleep(.1)
    print(f'{scroll} / {page_height}')


sleep(1)
print('Next Page Should be clicked now')
sleep(2)
# next_button_xpath = '/html/body/div[3]/div[2]/ul/li[11]/a'
next_button_xpath = '//ul[@class="pagination"]//li/a'
next_button = browser.find_elements(By.XPATH, next_button_xpath)

co_name_list = []

co_names = browser.find_elements(By.XPATH, '//tr[@class="exhibitors"]//a')
for co_name in co_names:
    co_name = co_name.text
    print(co_name)
    co_name_list.append(co_name)



#
# try:
#     i = 0
#     while i < 11:
#         next_button[-1].click()
#         i += 1
#         sleep(5)
#         print(f'Clicking on Next at {i}')
#         co_names = browser.find_elements(By.XPATH, '//tr[@class="exhibitors"]//a')
#         for co_name in co_names:
#             co_name = co_name.text
#             print(co_name)
#             co_name_list.append(co_name)
# except:
#     print('Not able to click on Next')

print(co_name_list)
df = pd.DataFrame(co_name_list)
print(df)

df.to_csv('malaysia.xlsx', index=False)









