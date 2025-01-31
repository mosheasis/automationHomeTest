from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def set_up():

    options = Options()
    # options.add_argument("--headless") # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox')  # # Bypass OS security model
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    options.add_argument("--start-fullscreen")
    options.add_argument('--disable-gpu')

    driver_web = webdriver.Chrome(options=options)

    return driver_web
