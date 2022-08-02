from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

opt = Options()
opt.add_experimental_option('debuggerAddress', 'localhost:9222')
# opt.add_argument('--headless')

browser = webdriver.Chrome(executable_path='chromedriver', options=opt)

url = 'https://www.linkedin.com/mynetwork/invite-connect/connections/'

browser.get(url)
sleep(2)




# height = browser.execute_script("return document.body.scrollHeight")
# for scroll in range(100, height, 100):
#     browser.execute_script(f"window.scrollTo(0,{scroll})")
#     sleep(0.1)


d_point_1_xpath = '//span[@class="mn-connection-card__name t-16 t-black t-bold"]'
d_point_1_elements = browser.find_elements(By.XPATH, d_point_1_xpath)


load_more_1 = browser.find_element(By.XPATH, '//div[@class="display-flex p5"]//button')
load_more_2 = browser.find_element(By.XPATH, '//div[@class="display-flex p5"]/button/span')
action = ActionChains(browser)
action.move_to_element(d_point_1_elements[-1])
sleep(1)
load_more_1.click()

sleep(1)
d_point_1_elements = browser.find_elements(By.XPATH, d_point_1_xpath)
action.move_to_element(d_point_1_elements[-1])


x = 0
for e in d_point_1_elements:
    d_point_1 = e.text
    print(d_point_1)
    x += 1

print(f'Total Data Points: {x}')

