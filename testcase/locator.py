from selenium.webdriver.common.by import By

class MainPageLocators():
    # By.IDでHTMLファイルのIDから属性の取得
    TEXT_BOX = (By.ID, "id-search-field")
    GO_BUTTON = (By.ID, "submit")

class SearchResultsPageLocators():
    pass