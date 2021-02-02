from time import sleep
from selenium import webdriver
import pyautogui

driver = webdriver.Chrome('C:\\Users\\pdr\\Documents\\repos\\botMeet\\chromedriver.exe')

f = open('password.txt', 'r')
f = f.readlines()
f[0] = f[0].replace('\n', '')
print(f)

driver.get('https://meet.google.com/')

sleep(3)

driver.find_element_by_xpath('/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a').click()

sleep(3)

driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(f[0])

driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()

sleep(3)

driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(f[1])

driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

sleep(3)

#link here
driver.get('https://meet.google.com/lookup/brtbsraiv6')

sleep(5)

driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span').click()

driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
                        

pyautogui.moveTo(388,183)

pyautogui.click()

sleep(0.5)

pyautogui.click()

sleep(2)

driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[1]/div[3]/div/div[2]/div[1]/span/span/div/div/span[1]').click()

sleep(1200)

i = True
while i:
    sleep(5)
    try:
        x = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[4]/div/div[2]/div[2]/div[1]/div[1]/span/div/span[2]')
        x = x.text.replace('(', '').replace(')', '')
        x = int(x)
        print('No momento tem: ' + str(x) + ' pessoas')
        if (x < 10):
            print('fechando...')
            driver.quit()
            i = False
    except:
        pass