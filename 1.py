from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  

driver.get("https://typekadeh.com")

account=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div/header/div/div/div[3]/button")
btn=account[0]
btn.click()

time.sleep(1)
signup=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/transition/div/div[2]/div/div/div/div[1]/form/div[2]")
btn=signup[0]
btn.click()

inputEmail=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/transition/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[1]/div/input")
txt=inputEmail[0]
txt.send_keys("zahramobasherai@gmail.com")

inputUsername=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/transition/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/input")
txt=inputUsername[0]
txt.send_keys("zmobasher")

inputPass=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/transition/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[3]/div/input")
txt=inputPass[0]
txt.send_keys("123123")

submit=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/transition/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[4]/div/button")
btn=submit[0]
btn.click()



# btns=dv.find_elements(By.TAG_NAME,"img")
# btn=btns[0]
# btn.click()
# inputs=driver.find_elements(By.ID,"main-search")
# txt=inputs[0]
# txt.send_keys("بارسا")
# time.sleep(5)



time.sleep(100)