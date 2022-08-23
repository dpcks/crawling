import imp
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# 크롬 옵션 객체 생성
options = webdriver.ChromeOptions()

# 크롬 브라우저 제어권 얻기
driver = webdriver.Chrome(
    service= Service(ChromeDriverManager().install()),
    options= options
)
driver.get("https://mwdeveloper.tistory.com/")
driver.implicitly_wait(5)



# 피드 클릭하기

driver.find_element(
    By.CSS_SELECTOR,
    '#mArticle > div:nth-child(3)'
).click()
for i in range(2,50):
    driver.find_element(
        By.CSS_SELECTOR,
        '#mArticle > div.area_paging > span > a.btn_next'
    ).click()
    driver.implicitly_wait(5)
    

# soup = BeautifulSoup(driver.)

driver.quit
  