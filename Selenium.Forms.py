from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Replace with the path to your WebDriver executable

# Navigate to the website
driver.get('https://www.example.com/form')

# Fill out the form
text_field = driver.find_element(By.NAME, 'text_field_name')
text_field.send_keys('Text input')

radio_button = driver.find_element(By.XPATH, '//input[@type="radio" and @value="radio_value"]')
radio_button.click()

checkbox = driver.find_element(By.NAME, 'checkbox_name')
checkbox.click()

# Submit the form
submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
submit_button.click()

# Wait for the success message to appear
success_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'success_message_id'))
)

# Verify that the success message is displayed
assert success_message.is_displayed()

# Close the browser window
driver.quit()