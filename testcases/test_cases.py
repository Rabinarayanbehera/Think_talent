"""test each textbox,checkbox,dropdown"""
from library.test_setup import *
from library.test_locatorts import *

def test_firstname(value,element="demo"):
    demo=driver.find_element(firstname).is_enabled()
    print(demo)
    demo.clear()
    demo.send_keys(value)
test_firstname("rabi")

def test_lastname(value):
    demo=driver.find_element(lastname).is_enabled()
    print(demo)
    demo.clear()
    demo.send_keys(value)

def test_email(value):
    demo=driver.find_element(email).is_enabled()
    print(demo)
    demo.clear()
    demo.send_keys(value)
def test_title(value):
    demo=driver.find_element(title).is_enabled()
    print(demo)
    demo.clear()
    demo.send_keys(value)

def test_site_domain(value):
    demo = driver.find_element(site_domain).is_enabled()
    print(demo)
    demo.clear()
    demo.send_keys(value)

def test_dropdown():
    demo = driver.find_element(dropdown).is_enabled()
    print(demo)

def test_checkbox():
    demo = driver.find_element(next).is_displayed()
    print(demo)

