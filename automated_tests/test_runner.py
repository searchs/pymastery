from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome("/usr/loc÷al/Caskroom/chromedriver/99.0.4844.51/chromedriver")
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# driver.maximize_window()
base_url = "https://demo.seleniumeasy.com/basic-first-form-demo.html"

driver.get(base_url)

assert "Selenium Easy Demo" in driver.title


show_message_button = driver.find_element(By.CLASS_NAME, "btn-default")
print(show_message_button.get_attribute("innerHTML"))

assert "Show Message" in driver.page_source

# user_message = driver.find_element_by_id("user-message")
user_message = driver.find_element(By.ID, "user-message")
user_message.clear()
user_message.send_keys("I am superdupercooool!")
print("What else do you want?")
show_message_button.click()
driver.quit()
