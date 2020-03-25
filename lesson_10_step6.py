import time
import math
from selenium import webdriver


def calc(x):
    return math.log(abs(12*math.sin(x)))

try: 
    link = "https://suninjuly.github.io/cats.html"
    browser = webdriver.Firefox()
    browser.get(link)

    browser.implicitly_wait(5)

    button = browser.find_element_by_id('button')
    
finally:
    time.sleep(10)
    browser.quit()