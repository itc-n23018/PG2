from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

message = input('URLを入力してください:')

MY_ADDRESS = 'YOUR_ID'
MY_PASSWORD = 'YOUR_PASSWORD'  

browser = webdriver.Chrome()
browser.get('https://mail.yahoo.co.jp')

WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'username'))
).send_keys(MY_ADDRESS)
browser.find_element(By.ID, 'btnNext').click()

WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, 'passwd'))
).send_keys(MY_PASSWORD)
browser.find_element(By.ID, 'btnSubmit').click()

WebDriverWait(browser, 15).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-cy="composeButton"]'))
).click()

WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-cy="composeToInput"]'))
).send_keys(to_address + '\n')

browser.find_element(By.CSS_SELECTOR, 'input[data-cy="composeSubjectInput"]').send_keys('自動送信')
browser.find_element(By.CSS_SELECTOR, 'textarea[data-cy="composeBody"]').send_keys(message)

browser.find_element(By.CSS_SELECTOR, 'button[data-cy="composeSendMailButton"]').click()
