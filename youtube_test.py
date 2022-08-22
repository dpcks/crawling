import time
from typing import KeysView 
from selenium.webdriver.common.by import By # 요소를 어떤 방식으로 선택할지에 대한 상수값이 있다.
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버 관리
from selenium import webdriver # 실제 브라우저를 조작
# from selenium.webdriver.chrome.service import Service  # 자동완성기능

options = webdriver.ChromeOptions() # 크롬 옵션 객체

# 크롬 드라이버 생성 및 크롬 제어권 얻기
driver = webdriver.Chrome(
    service = webdriver.chrome.service.Service(ChromeDriverManager().install())
)


driver.get("https://www.youtube.com/")
#time.sleep(5) # 인수 값을 초단위
driver.implicitly_wait(5) # 웹 리소스가 모두 로딩되면 다음으로 넘어간다.

# 검색어 입력 
driver.find_element(
    By.XPATH,
    '//input[@id = "search"]'
).send_keys("오은영 레전드")
time.sleep(2)

# 검색 버튼 클릭
driver.find_element(
    By.XPATH,
    '//*[@id="search-icon-legacy"]'
).click()
time.sleep(5)
# driver.implicitly_wait(5)

# 첫번쪠 동영상 틀기
driver.find_element(
    By.XPATH,
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[3]/div[1]/ytd-thumbnail/a'
).click()
time.sleep(5)

# 광고 스킵 클릭
driver.find_element(
    By.CSS_SELECTOR,
    '.ytp-ad-skip-button'
).click()

# 동영상 시청을 위해 대기
time.sleep(10)

driver.quit() # 브라우저 닫기
