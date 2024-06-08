from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_web_driver(url: str, option=None) -> object:
    """WebDriverを生成する"""
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.get(url)
    return driver


def disconnect(driver):
    """WebDriverを切断する"""
    driver.close()
    print("WebDriverは切断されました。")


def get_element_by_id(driver, id_attr):
    """指定した「id」属性の要素を1つ取得する"""
    return driver.find_element(By.ID, id_attr)


def get_element_by_class(driver, class_attr):
    """指定した「class」属性の要素を1つ取得する"""
    return driver.find_element(By.CLASS_NAME, class_attr)


def get_elements_by_classes(driver, class_attr):
    """指定した「class」属性の要素を全て取得する()"""
    return driver.find_elements(By.CLASS_NAME, class_attr)


def get_element_by_linktext(driver, class_attr):
    """指定した「a」属性の要素を1つ取得する"""
    return driver.find_element(By.LINK_TEXT, class_attr)


def switch_browser_tabs(driver):
    """ブラウザのタブを右に1つ移動する"""
    driver.switch_to.window(driver.window_handles[1])


def push_button_in_javascript(driver, js_code):
    """javascriptが埋め込まれたボタンを押下する

    サンプル:<input type="button" value="Excel" onclick="javascript:excelout()">
    """
    driver.execute_script(js_code)


def push_link_anchor_text(driver, link_elem):
    """aタグのリンク(ボタン)を押下する

    サンプル:<input type="button" value="Excel" onclick="javascript:excelout()">
    """
    driver.execute_script("arguments[0].click();", link_elem)
