from locator import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage():
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def input_text_box(self):
        WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located((MainPageLocators.TEXT_BOX))
        )
        # "*"をMainPageLocators.TEXT_BOXの前に付けることで、2MainPageLocators.TEXT_BOXの中にある2つの要素(By.ID, "id-search-field")を展開してくれる。
        element = self.driver.find_element(*MainPageLocators.TEXT_BOX)
        element.send_keys("ああああ" + Keys.ENTER)

    def click_go_button(self):
        WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located((MainPageLocators.GO_BUTTON))
        )
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()
        
class SearchResultsPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source