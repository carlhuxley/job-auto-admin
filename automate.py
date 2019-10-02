import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 3


class App_page():

    @staticmethod
    def page_get(url):
        driver.get(url)
        driver.implicitly_wait(3)

    @staticmethod
    def click_link(link_text):
        element = driver.find_element_by_link_text(link_text)
        actions = ActionChains(driver)
        actions.click(element)
        actions.perform()
        driver.implicitly_wait(3)

    @staticmethod
    def click_id(elem_id):
        element = driver.find_element_by_id(elem_id)
        actions = ActionChains(driver)
        actions.click(element)
        actions.perform()
        driver.implicitly_wait(3)

    @staticmethod
    def click_xpath(elem_xpath):
        element = driver.find_element_by_xpath(elem_xpath)
        actions = ActionChains(driver)
        actions.click(element)
        actions.perform()
        driver.implicitly_wait(3)

    @staticmethod
    def send_keys_id(elem_id, elem_text):
        element = driver.find_element_by_id(elem_id)
        driver.find_element_by_id(elem_id).send_keys(elem_text)
        driver.implicitly_wait(3)

    @staticmethod
    def run_steps(steps_list):
        for step in steps_list:
            step
