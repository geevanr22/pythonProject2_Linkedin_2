from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option('debuggerAddress', 'localhost:9222')
# opt.add_argument('--headless')

browser = webdriver.Chrome(executable_path='chromedriver', options=opt)

url = ''
xpath = ''
browser.get(url)
elements = browser.find_elements(By.XPATH, xpath)

for element in elements:
    print(element.text)