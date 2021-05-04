# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test122(self):
    # Test name: test 122
    # Step # | name | target | value
    # 1 | open | http://www.google.com | 
    self.driver.get("http://www.google.com")
    # 2 | setWindowSize | 1268x668 | 
    self.driver.set_window_size(1268, 668)
    # 3 | click | name=q | 
    self.driver.find_element(By.NAME, "q").click()
    # 4 | type | name=q | youtube
    self.driver.find_element(By.NAME, "q").send_keys("youtube")
    # 5 | click | css=.LLD4me | 
    self.driver.find_element(By.CSS_SELECTOR, ".LLD4me").click()
    # 6 | click | css=center:nth-child(1) > .gNO89b | 
    self.driver.find_element(By.CSS_SELECTOR, "center:nth-child(1) > .gNO89b").click()
    # 7 | click | css=.cfxYMc | 
    self.driver.find_element(By.CSS_SELECTOR, ".cfxYMc").click()
  