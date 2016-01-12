#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math

### THIS ASSUMES YOU NEVER CHANGE THE VELOCITY FACTOR FROM 95% ###

driver = webdriver.Firefox()
driver.get('http://www.kg7hsn.com')

def main():
    check_title('KG7HSN')
    find_click_link('Dipole')
    update_dipole_field('14.076')
    rc = check_dipole_calculations(14.076)
    driver.close()

def check_title(t=None):
    assert t in driver.title
    time.sleep(.5)

def find_click_link(val=None):
    element = driver.find_element_by_partial_link_text(val)
    element.click()
    time.sleep(.5)

def update_dipole_field(val=None):
    element = driver.find_element_by_xpath("//input[@name='mhz']")
    element.send_keys(val)
    time.sleep(1)
    element.submit()
    time.sleep(2)

def check_dipole_calculations(mhz):
    feet = (((300/mhz)/4)*(95*0.01)*3.28084)
    feet = int(math.floor(feet))
    assert str(feet)+" feet" in driver.page_source

if __name__ == "__main__":
    main()
