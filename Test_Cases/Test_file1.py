from selenium import webdriver



class Test_pytest:

    def test_sum_001(self):

        a = 1
        b = 2
        sum = a+b
        print(sum)
        if sum == 4:
            assert True
        else:
            assert False

    def test_sum_002(self):

            a = 1
            b = 2
            sum = a + b
            print(sum)

    def test_credence_url_003(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("you are at right place")
        else:
            print("you are wrong place")