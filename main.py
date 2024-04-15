from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)

# googleにアクセス
driver.get("https://www.google.com")
# 検索結果を表示して5秒後ウインドウを閉じる
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
# google検索窓から"Selenium"を入力 + ENTERキー → 検索
input_element.send_keys("Selenium" + Keys.ENTER)

# 検索後、指定した結果をクリック＆遷移
# LINK_TEXT = 完全一致
# PARTIAL_LINK_TEXT = 一部一致
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Selenium"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium")
link.click()

# 10秒後ウィンドウ閉じる
time.sleep(10)
driver.quit()
