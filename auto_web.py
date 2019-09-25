from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

class User:
    def __init__(self, submit_btn_path, account_btn_class, logout_url, email_field_id, password_field_id, login_url, email, password):
        self.submit_btn_path = submit_btn_path
        self.account_btn_class = account_btn_class
        self.logout_url = logout_url
        self.email_field_id = email_field_id
        self.password_field_id = password_field_id
        self.login_url = login_url
        self.email = email
        self.password = password
        
    def login(self):
        driver.get(self.login_url)
        driver.find_element_by_id(self.email_field_id).send_keys(self.email)
        driver.find_element_by_id(self.password_field_id).send_keys(self.password)
        driver.find_element_by_xpath(self.submit_btn_path).click()
        
    def logout(self):
        driver.get(self.logout_url)
       


