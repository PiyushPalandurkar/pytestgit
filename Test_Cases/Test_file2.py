import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_pytest:

    def test_sum_004(self):

        a = 1
        b = 2
        sum = a+b
        print(sum)
        if sum == 3:
            assert True
        else:
            assert False

    def test_sum_005(self):

            a = 1
            b = 2
            sum = a + b
            print(sum)

    def test_credence_006(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("https://credence.in/")
        driver.find_element(By.XPATH,"//img[@src='/website/images/enquiry.png']").click()
        l=len(driver.find_elements(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a"))
        # print(l)
        contact_number_list=[]
        for r in range(1, l+1):
            contact_number= driver.find_element(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a[" +str(r)+"]").text
            # print(contact_number)
            contact_number_list.append(contact_number)
        print(contact_number_list)
        if "+91 9579064658" in contact_number_list:
            print(contact_number_list.index("+91 9579064658"))
            assert True
        else:
            assert False




        # if driver.title == "Credence":
        #     print("you are at right place")
        # else:
        #     print("you are wrong place")
