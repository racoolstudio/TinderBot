# import os for environment variable
import os
# import the time module to delay the code
import time
# import selenium which gets the automation done
from selenium import webdriver
from selenium.webdriver.common.by import By
# get the location of the chrome driver path
chrome_driver_path = '/Users/racool/Desktop/chromedriver'
# create a webdriver object then assign the location for driver
driver = webdriver.Chrome(chrome_driver_path)
# assign the tinder link to variable link
link = 'https://tinder.com/'
# declare phone number to a variable phone_number to sign in to tinder
phone_number = os.getenv('PHONE')
# get the website
driver.get(link)
# delay for 2 secs
time.sleep(2)
# find the privacy button then accept
driver.find_elements(By.CSS_SELECTOR, '#t-188693591 div div div div div button')[-3].click()
# click on the login button
driver.find_elements(By.CLASS_NAME, 'l17p5q9z')[1].click()
# delay for a sec so it can load the page
time.sleep(1)
# find the sign in by phone  number. You can use other options
driver.find_element(By.XPATH, '//*[@id="t-1917074667"]/main/div/div[1]/div/div/div[3]/span/div[3]/button').click()
# delay for 5 secs so it could load
time.sleep(5)
# get the phone number element and enter you phone number
driver.find_element(By.NAME, 'phone_number').send_keys(phone_number)
# click on the continue button
driver.find_elements(By.CSS_SELECTOR, '.Expand div button')[-2].click()
# delay for 1 min for verification process
time.sleep(60)
# click on allow location
driver.find_elements(By.CSS_SELECTOR, '.onboarding__modal div button')[0].click()
# click on not interested in notification
driver.find_element(By.XPATH, '//*[@id="t-1917074667"]/main/div/div/div/div[3]/button[2]').click()
# delay for 8 secs to find people near you
time.sleep(8)
# declare the number of swipes you want to like
num_of_swipes = 98

for i in range(98):
    # delay for 2 sec to load the next page
    time.sleep()
    # like
    driver.find_elements(By.CSS_SELECTOR, '.Bd button ')[-2].click()
