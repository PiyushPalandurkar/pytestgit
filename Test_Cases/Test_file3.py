import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_pytest:

    def test_ORANGEHRM_007(self):
        driver = webdriver.Chrome()

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        driver.find_element(By.NAME, "username").send_keys("Admin")

        driver.find_element(By.NAME, "password").send_keys("admin123")

        driver.find_element(By.CLASS_NAME, "oxd-button").click()

        driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()

        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()






        try:
            driver.find_element(By.XPATH, "//div[@class='oxd-topbar-header-title']")
            print("successful")
        except:
            print("Failed")
    def test_Registration_008(self):
        driver = webdriver.Firefox()
        driver.find_element(By)




        # if driver.title == "Credence":
        #     print("you are at right place")
        # else:
        #     print("you are wrong place")
