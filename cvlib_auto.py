# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 10:40:50 2019

@author: Carl Huxley
"""
import os
import pyautogui
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 3
from selenium.webdriver.common.action_chains import ActionChains
from auto_web import User, driver

EMAIL_USER = os.environ.get('EMAIL_USER')
CVLIB_PASS = os.environ.get('CVLIB_PASS')
TJOBS_PASS = os.environ.get('TJOBS_PASS')

submit_btn_path = "//*[@id='cand-login-left']/input[3]"
account_btn_class = 'a.profile-name-header'
logout_url = 'https://www.cv-library.co.uk/candidate/logout'
tjlogout_field_id = ""
email_field_id = "cand_email"
password_field_id = "cand_password"
login_url = 'https://www.cv-library.co.uk/candidate/login'

tjsubmit_btn_path = '//*[@id="btnLogin"]'
tjaccount_btn_class =""
tjlogin_url = "https://www.totaljobs.com/account/signin?ReturnUrl=/"
tjlogout_url = 'https://www.totaljobs.com/account/signout?ReturnUrl=/'
tjemail_field_id = 'Form_Email'
tjpassword_field_id = 'Form_Password'

class Automate(User):
    def __init__(self, submit_btn_path, account_btn_class, logout_url, email_field_id, password_field_id, login_url, email, password):
        super().__init__(submit_btn_path, account_btn_class, logout_url, email_field_id, password_field_id, login_url, email, password)
    
    @staticmethod
    def change_cover_letter():
        menu = driver.find_element_by_link_text("My CV")
        hover = ActionChains(driver).move_to_element(menu)
        hover.perform()
        hidden_submenu = driver.find_element_by_link_text("Cover Letters")
        actions = ActionChains(driver)
        actions.click(hidden_submenu)
        actions.perform()
        
    @staticmethod    
    def upload_cv():
        menu = driver.find_element_by_link_text("My CV")
        hover = ActionChains(driver).move_to_element(menu)
        hover.perform()
        hidden_submenu = driver.find_element_by_link_text("Modify CV")
        actions = ActionChains(driver)
        actions.click(hidden_submenu)
        actions.perform()
        driver.find_element_by_xpath('//*[@id="modify_form"]/div[1]/section[2]/div[2]').click()
        device = driver.find_element_by_id('filepicker-device')
        click_device = ActionChains(driver)
        click_device.click(device)
        click_device.perform()
        
        pyautogui.typewrite(['tab', 'tab', 'tab', 'tab', 'tab', 'enter'])
        pyautogui.write('C:/Files/Carl/Career/CVs/Master/')
        pyautogui.typewrite(['enter'])
        pyautogui.typewrite(['tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'enter'])
        pyautogui.write('2019_09_02_Carl_Huxley_CV.docx')
        pyautogui.typewrite(['enter'])
        
        up_btn = driver.find_element_by_id('upload-new-cv')
        click_upload = ActionChains(driver)
        click_upload.click(up_btn)
        click_upload.perform()  
      
cvlib_auto = Automate(submit_btn_path, account_btn_class, logout_url, email_field_id, password_field_id, login_url, EMAIL_USER, CVLIB_PASS)
cvlib_auto.login()
cvlib_auto.upload_cv()
#cvlib_auto.change_cover_letter()

#cvlib_auto.logout()

#tj_login = User(tjsubmit_btn_path, tjaccount_btn_class, tjlogout_url, tjemail_field_id, tjpassword_field_id, tjlogin_url, email, totaljobspw)
#tj_login.login()
#tj_login.logout()

#job_apply(job_url)
#driver.close()
#driver.quit()

