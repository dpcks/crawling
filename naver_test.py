import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# 크롬 옵션 객체 생성
options = webdriver.ChromeOptions()
# options.add_argument("--headless") # 창 없이 실행하기
# options.add_argument("user agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
options.add_argument("--start-fullscreen") # 전체화면

# 크롬 브라우저 제어권 얻기
driver = webdriver.Chrome(
    service= Service(ChromeDriverManager().install()),
    options= options
)
driver.get("https://www.naver.com")
driver.implicitly_wait(5)


# 검색어 입력칸
driver.find_element(
    By.CSS_SELECTOR,
    "#query"
).send_keys("빅데이터와 인공지능")


# 검색버튼 클릭
driver.find_element(
    By.CSS_SELECTOR,
    "#search_btn"
).click()
time.sleep(2)

# 지식인 메뉴 클릭하기 
driver.find_element(
    By.CSS_SELECTOR,
    "#lnb > div.lnb_group > div > ul > li:nth-child(4)"
).click()
time.sleep(5)
driver.get_screenshot_as_file("naver_kin_page1.png")

# 지식인 페이지의  텍스트만 가죠오기
## 드라이버 객체의 페이지 소스를 soup 객체로 변환
soup = BeautifulSoup(driver.page_source,"html.parser")
contents = soup.select_one("._au_kin_collection") # 지식인 부분만
contents_dict = {
    1 : contents.text # 태그를 제외한 텍스트만 value로 저장
}


# 5페이지 까지 반복
for i in range(2,6):
    driver.find_element(
        By.CSS_SELECTOR,
        '#main_pack > div.api_sc_page_wrap > div > a.btn_next'
    ).click()
    driver.implicitly_wait(5)
    driver.get_screenshot_as_file(f"naver_kin_page{i}.png") # 스크린샷 찍기
    

    soup = BeautifulSoup(driver.page_source,"html.parser")
    contents = soup.select_one("._au_kin_collection") # 지식인 부분만
    contents_dict[i]= contents.text # 태그를 제외한 텍스트만 value로 저장
    
# json 저장하기
import json
with open("contents.json","w",encoding="utf-8") as f:
    json.dump(contents_dict,f,ensure_ascii=False,indent=4)

driver.quit()