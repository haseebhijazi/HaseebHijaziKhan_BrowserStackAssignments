from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
import time


options = ChromeOptions()

driver = webdriver.Chrome(options=options)

driver.get("https://www.flipkart.com/")

print(driver.title)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input"))).click()

active_ele = driver.switch_to.active_element
active_ele.send_keys("Samsung Galaxy S10")
active_ele.send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div[1]/div[1]/div/div[1]/div/div/section/div[3]/div/a"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div[1]/div[1]/div/div[1]/div/section[3]/div[2]/div/div/div/label/div[2]"))).click()
time.sleep(2)
element = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div[1]/div/div[1]/div/section[4]/label/div[2]")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
driver.execute_script("arguments[0].click();", element)
time.sleep(2)
element2= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div[4]")))
driver.execute_script("arguments[0].scrollIntoView(true);", element2)
driver.execute_script("arguments[0].click();", element2)

time.sleep(2)

divs = driver.find_elements(By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div")

for i, div in enumerate(divs):
    if "cPHDOP" not in div.get_attribute("class"):
        continue

    if "75nlfW" not in div.find_element(By.XPATH, "div").get_attribute("class"):
        continue

    print(f"Item {i}:", end=" ")
    print("Product Name" ,end="->")
    try:
        print(div.find_element(By.XPATH, "div/div/div/a/div[2]/div[1]/div[1]").text)
    except NoSuchElementException:
        print("Product Name not found")


    print("Price",end="->")
    try:
        print(div.find_element(By.XPATH, "div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]").text)
    except NoSuchElementException:
        print("Price not found")
    print("Link to Product Details Page",end="->")
    try:
        print(div.find_element(By.XPATH, "div/div/div/a").get_attribute("href"))
    except NoSuchElementException:
        print("Link not found")

    print()

driver.close()
