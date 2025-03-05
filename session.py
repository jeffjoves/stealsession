from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from tabulate import tabulate

# Set up WebDriver (use headless mode if needed)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background (optional)
driver = webdriver.Chrome(options=options)

# Open the login page
driver.get("https://jeffjoves.github.io/paypal/")

# Simulate user login (modify based on website fields)
email_input = driver.find_element(By.ID, "email")  # Find email field
password_input = driver.find_element(By.ID, "password")  # Find password field
login_button = driver.find_element(By.ID, "login")  # Find login button

email_input.send_keys("test@example.com")  # Replace with test credentials
password_input.send_keys("password123")  # Replace with test credentials
login_button.click()  # Click login button

time.sleep(3)  # Wait for login to process

# Get cookies
cookies = driver.get_cookies()

# Format data for table
cookie_data = [[cookie["name"], cookie["value"]] for cookie in cookies]

# Print cookies in table format
if cookie_data:
    print(tabulate(cookie_data, headers=["Cookie Name", "Value"], tablefmt="grid"))
else:
    print("No cookies found.")

# Close the browser
driver.quit()
