# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element_by_id('user-name').send_keys(user)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login-button').click()
    assert 'https://www.saucedemo.com/inventory.html' in driver.current_url    
    print(f'Login with username {user} and password {password} successfully.')

def add_cart(driver, n):
    for i in range(n):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element_by_css_selector(element).click()
        driver.find_element_by_css_selector("button.btn_primary.btn_inventory").click()
        product = driver.find_element_by_css_selector("div[class='inventory_details_name']").text
        print(product + " added to shopping cart.")
        driver.find_element_by_css_selector("button.inventory_details_back_button").click()
    print(f'{n} items are all added to shopping cart successfully.')

def remove_cart(driver, n):
    for i in range(n):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element_by_css_selector(element).click()
        driver.find_element_by_css_selector("button.btn_secondary.btn_inventory").click()
        driver.find_element_by_css_selector("button.inventory_details_back_button").click()
    print(f'{n} items are all removed from shopping cart successfully.')


if __name__ == "__main__":
    n = 6
    username = 'standard_user'
    password = 'secret_sauce'
    driver = login(username, password)
    add_cart(driver, n)
    remove_cart(driver, n)
    print('Check passed!')

