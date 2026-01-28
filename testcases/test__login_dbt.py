import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import  By
from pageObjects.LoginPage import Login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from  utilities import XLUtils

class Test_002_DDT_Login:
    baseURL =ReadConfig.getApplicationURL()
    path =".//TestData//logindata.xlsx"

    logger = LogGen.loggen()# calling the methodd and beacuse static method it call by classname

    @pytest.mark.regression
    def test_login_dbt(self,setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.rows=XLUtils.getRowCount(self.path,"Sheet1")
        print(self.rows)
        lst_status =[]
        for r in range(2,self.rows+1):
            self.user =XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.expected = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("test is pass")
                    self.lp.ClickLogout()
                    lst_status.append("passed")
                elif self.exp == "Fail":
                    self.logger.info("test is pass")
                    self.lp.ClickLogout()
                    lst_status.append("Fail")
            elif act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***fail***")

                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("test is pass")

                    lst_status.append("pass")
        if "Fail" not  in lst_status:
                self.logger.info("LoginDDTtestpassed")
                self.driver.close()
                assert True
        else:
                self.logger.info("Loggin dbt is failed")
                self.driver.close()
                assert False

