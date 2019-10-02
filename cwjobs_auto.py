# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 10:40:50 2019

@author: Carl Huxley
"""
import os
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
from auto_web import User, driver

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 3

EMAIL_USER = os.environ.get('EMAIL_USER')
CWJOB_PASS = os.environ.get('CWJOB_PASS')

job_url = 'https://www.cwjobs.co.uk/job/senior-automation-tester/amsource-technology-ltd-job88042045'
submit_btn_path = '//*[@id="btnLogin"]'
account_btn_class = 'a.profile-name-header'
logout_url = 'https://www.cwjobs.co.uk/account/signout?ReturnUrl=/'
email_field_id = "Form_Email"
password_field_id = "Form_Password"
login_url = 'https://www.cwjobs.co.uk/account/signin?ReturnUrl=/'


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
        pyautogui.write('2019_09_26_Carl_Huxley_CV.docx')
        pyautogui.typewrite(['enter'])

        up_btn = driver.find_element_by_id('upload-new-cv')
        click_upload = ActionChains(driver)
        click_upload.click(up_btn)
        click_upload.perform()

    @staticmethod
    def job_apply(url):
        driver.get(url)
        apply_btn = driver.find_element_by_link_text('APPLY')
        actions = ActionChains(driver)
        actions.click(apply_btn)
        actions.perform()
        add_cover_letter = driver.find_element_by_id('coverLetterText')
        actions = ActionChains(driver)
        actions.click(add_cover_letter)
        actions.perform()
        submit = driver.find_element_by_id('btnSubmit')
        actions = ActionChains(driver)
        actions.click(submit)
        actions.perform()


#cwjobs_auto = Automate(submit_btn_path, account_btn_class, logout_url, email_field_id, password_field_id, login_url, EMAIL_USER, CWJOB_PASS)
#cwjobs_auto.login()
# cwjobs_auto.upload_cv()
# cvlib_auto.change_cover_letter()
#cwjobs_auto.job_apply(job_url)
# cwjobs_auto.logout()
# job_apply(job_url)
# driver.close()
# driver.quit()
