import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    #Add Customer Page
    lnkCustomer_menu_xpath = "/html/body/div[3]/aside/div/nav/ul/li[4]/a"
    lnkCustomer_menuitem_xpath = "/html/body/div[3]/aside/div/nav/ul/li[4]/ul/li[1]/a"
    btnAddnew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtEmail_xpath = "//*[@id='Email']"
    txtPassword_xpath = "//*[@id='Password']"
    txtcustomerRoles_xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/span/span[1]/span/ul"
    listitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    listitemRegistered_Xpath = "//li[contains(text(),'Registered')]"
    listitemsGuests_xpath = "//li[contains(text(),'Guests')]"
    listitemsVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleFender_id = "Gender_Female"
    txtFirstName_xpath = "//*[@id='FirstName']"
    txtLastName_xpath = "//*[@id='LastName']"
    # txtDob_xpath = ""
    txtCompanyName_xpath = "//*[@id='Company']"
    txtAdminContent_xpath = "//*[@id='AdminComment']"
    btnSave_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role=='Registered':
            self.listitem=self.driver.find_element_by_xpath(self.listitemRegistered_Xpath)
        elif role=='Adminstrators':
            self.listitem=self.driver.find_element_by_xpath(self.listitemAdministrators_xpath)
        elif role=='Vendors':
            self.listitem=self.driver.find_element_by_xpath(self.listitemsVendors_xpath)
        else:
            self.listitem=self.driver.find_element_by_xpath(self.listitemsGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("argument[0].click();",self.listitem)




