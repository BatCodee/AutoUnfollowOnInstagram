# -*- coding: utf-8 -*-
"""
Spyder Editor

Script to automatic unfollow on Instagram
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\user\Downloads\Learning\chromedriver.exe")
driver.maximize_window()
driver.get('https://instagram.com')
driver.implicitly_wait(5)
driver.find_element_by_name("username").send_keys("username")
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
driver.find_element_by_xpath('//a[img/@src="link of your profile pixture. Just inspect it and copy the href"]').click()
time.sleep(5.0)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
driver.find_element_by_xpath('/html/body/div[4]/div/div/nav/a[2]/span').click() #Navigating to Hashtags. You can delete this if you want to unfollow profile,
driver.find_element(By.XPATH, '//button[text()="Following"]').click()           #clicking unfollow button
time.sleep(5.0)
driver.close()
