import argparse
import time
import sys, getopt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


driver = None


 # change it!

def launch():
  print("Loading...")
  global driver
  # driver = webdriver.PhantomJS("phantomjs-2.0.0-windows\\bin\\phantomjs.exe")
  driver = webdriver.Chrome('/home/rkc/Projects/Flask/chromedriver')
  driver.get('https://web.skype.com/en')
  driver.set_window_size(1024, 768)
  print("Loaded Skype!")

def signIn():
  countval = 1;
  counterli = 1
  print("Entered Skype!")
  userNameField = driver.find_element_by_id("username")
  userNameField.clear()
  userNameField.send_keys('a4yush1')
  driver.find_element_by_xpath('//*[@id="signIn"]').click()
  time.sleep(2)
  passwordField = driver.find_element_by_id("i0118")
  passwordField.clear()
  passwordField.send_keys('Apr2indore')
  # //*[@id="CredentialsInputPane"]/div[2]/div/div/div[5]/div/div/div[2]
  # //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[2]
  driver.find_element_by_xpath('//*[@id="CredentialsInputPane"]/div[2]/div/div/div[5]/div/div/div[2]').click()
  time.sleep(2)
  print("Signed In!")
  time.sleep(12)
  driver.find_element_by_xpath('//*[@id="menuItem-contacts"]/span[1]/span').click()
  print("Contacts Loaded!")
  time.sleep(2)
  count = driver.find_elements_by_xpath('//*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div')
  length = len(count)
  print(length)
  for i in count:
      countval = countval+1
      counterli = 1;
      print(countval)
      maxli = driver.find_elements_by_xpath('//*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[{}]/div/li'.format(countval))
      for j in maxli:
          try:
            driver.find_element_by_xpath('//*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[{}]/div/li[{}]'.format(countval,counterli)).click()
            print(counterli)
            counterli = counterli+1
            InputBox = driver.switch_to_active_element()
            InputBox.clear()
            print("Message data worked!")
            InputBox.send_keys("Hello!")
            driver.find_element_by_xpath('//*[@id="menuItem-contacts"]/span[1]/span').click()
          except NoSuchElementException:
            break
  # isElement = check_element('//*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[{}]/div/li[4]'.format(countval))
  # isElement = check_element('//*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[2]/div/li[7]')
  # print(isElement)
  # if isElement == True:
  #   print("done")
  # else:
  #   print('error')

def signOut():
  print("Signing out...")
  if not driver.find_element_by_class_name("signOut").is_displayed():
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME,'summary'))).click()
  WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME,'signOut'))).click()
  print("Signed Out!")

# def quit():
#   print("Quitting...")
#   driver.quit()

def check_element(locator):
  try:
      driver.find_element_by_xpath(locator)
  except NoSuchElementException:
      print ('No such thing')
      return False
  return True

def main(args):
  try:
    launch()
    signIn()
  except:
    print("Something went wrong")
  finally:
    quit()


if __name__ == "__main__":
  print("Starting up...")
  parser = argparse.ArgumentParser(description='pySkypeBot: Python Skype Bot')
  parser.add_argument('-ytexpert', '--username', help='Skype User Name')
  parser.add_argument('-fucking<3', '--password', help='Skype Password')
  main(parser.parse_args())