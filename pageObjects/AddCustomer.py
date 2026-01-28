from selenium.webdriver.support.ui import Select
import time

class AddCustomer:
    InkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    InkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password' ]"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap' ]"
    IstitemAdministrators_xpath = "//li[contains(text(), 'Administrators')]"
    IstitemRegistered_xpath = "//li[contains(text(), 'Registered' )]"
    IstitemGuests_xpath = "//li[contains(text(), 'Guests')]"
    IstitemVendors_xpath = "//li[contains(text(), 'Vendors' )]"
    drpmgr0fVendor_xpath = "//*[@id= 'VendorId' I"
    raMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName' ]"
    txtLastName_xpath = "//input[@id='LastName' ]"
    txtDob_xpath = "//input[@id='Date0fBirth']"
    txtCompanyName_xpath = "//input[@id='Company' ]"
    txtAdminContent_xpath = "//textarea[@id='AdminComment' ]"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickonCustomersMenu(self):
        self.driver.find_element_by_xpath(self.InkCustomers_menu_xpath).click()

    def clickonCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.InkCustomers_menuitem_xpath).click()

    def clickonAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
         self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setDob(self,dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickonSave(self):
         self.driver.find_element_by_xpath(self.btnSave_xpath).click()

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.IstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.IstitemAdministrators_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRolelds_taglist'l/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.IstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.IstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.IstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.IstitemGuests_xpath)
            time.sleep(3)
            self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setgender(self,gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdFeMaleGender_id).click()
        else:
           self.driver.find_element_by_id(self.rdMaleGender_id).click()