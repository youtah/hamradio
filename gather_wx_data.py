import os
import re
import sys
import time
import json
from selenium import webdriver

def main(args):
    chromedriver = "C:\Users\Jeff\Desktop\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get('http://k7msh-lakemountain-wx.local.mesh/');
    html = strip_encoded_chars(driver.page_source)
    make_json(html)
    driver.quit()

def make_json(html):
    try:
        data = {}
        data['windSpeed']               = get_wind_speed(html)
        data['windKnots']               = get_wind_knots(html)
        data['windDirection']           = get_direction(html)
        data['windDirectionCompass']    = get_compass_direction(html)
        data['windStrength']            = get_strength(html)
        data['tempInside']              = get_temp_inside(html)
        data['tempOutside']             = get_temp_outside(html)
        json_data = json.dumps(data)
        print str(json_data)
        return json_data
    except Exception as err:
        print "Failed creating JSON object: "+str(err)
        raise err

def get_wind_speed(html):
    m = re.search('Speed: (\d*\.\d*)', html)
    return str(m.group(1)).strip()

def get_wind_knots(html):
    m = re.search('Knots: (\d*\.\d*)', html)
    return str(m.group(1)).strip()

def get_strength(html):
    m = re.search('Strength: (.*)<br />', html)
    return str(m.group(1)).strip()

def get_direction(html):
    m = re.search('Direction: (\d*)<br />', html)
    return str(m.group(1)).strip()

def get_compass_direction(html):
    m = re.search('Compas Direction: (\D*)<br />', html)
    return str(m.group(1)).strip()

def get_temp_inside(html):
    m = re.search('Temp inside building: (\d*\.\d*)', html)
    return str(m.group(1)).strip()

def get_temp_outside(html):
    m = re.search('temp outside building: (\d*\.\d*)', html)
    return str(m.group(1)).strip()

def strip_encoded_chars(html):
    try:
        ascii_html = html.encode('ascii', 'ignore').decode('ascii')
        return ascii_html
    except Exception as err:
        print "Failed to strip encoded chars: "+str(err)
        raise err

if __name__ == '__main__':
    main(sys.argv)
