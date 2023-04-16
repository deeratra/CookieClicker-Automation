from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import re

PATH = "D:\Deepankar\Coding beginners\Moment\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--ignore-certificate-errors")
service = ChromeService(executable_path=PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://orteil.dashnet.org/cookieclicker/")
try:
    options_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fc-button-label"))
    )
    options_button.click()

    lang_select_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN"))
    )

    lang_select_button.click()
    cookie = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )
    cookie_count = driver.find_element(By.ID, "cookies")
    items_list = ["productPrice" + str(i) for i in range(4, -1, -1)]
    print(items_list)

    actions = ActionChains(driver)

    for i in range(1000):
        actions.click(cookie)
        actions.perform()
        count = int(cookie_count.text.split(" ")[0])
        for items in items_list:
            value = driver.find_element(By.ID, str(items))
            mileStone = value.text
            mileStone = re.sub("[^\d\.]", "", mileStone)
            if mileStone != "" and int(mileStone) <= count:
                purchase = ActionChains(driver)
                purchase.move_to_element(value)
                purchase.click()
                purchase.perform()
except Exception as e:
    print(e)
finally:
    driver.quit()
