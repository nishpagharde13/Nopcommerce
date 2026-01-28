import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import  By
from pageObjects.LoginPage import Login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL =ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()# calling the methodd and beacuse static method it call by classname

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("******Test__001__Login**********")
        self.logger.info("******Verify home page title**********")
        self.driver = setup
        print("Base URL from config:", self.baseURL)
        self.driver.get(self.baseURL)

        if act_title == "nopCommerce demo store. Login":
            self.driver.close()
            assert True
            self.logger.info("******Test is passed**********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title= self.driver.title
        print(act_title)
        time.sleep(30)
        if act_title == "Dashboard / nopCommerce administration":
            time.sleep(20)
            print("Actual title:", act_title)

            assert True
        else:

            assert False









