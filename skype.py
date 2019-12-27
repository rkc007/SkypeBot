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

# driver = webdriver.Chrome('/home/rkc/Projects/Flask/chromedriver')

# def launch():
print("Loading...")
global driver
# driver = webdriver.PhantomJS("phantomjs-2.0.0-windows\\bin\\phantomjs.exe")
driver = webdriver.Chrome('/home/rkc/Projects/Flask/chromedriver')
driver.get('https://web.skype.com/en')
driver.set_window_size(1024, 768)
print("Loaded Skype!")

userName = 'username'    # change it!
password = 'password' # change it!

# def signIn(userName, password):
print("Signing in...")
userNameField = driver.find_element_by_id("username")
userNameField.clear()
userNameField.send_keys(userName)
# //*[@id="CredentialsInputPane"]/div[2]/div/div/div[4]/div/div/div[2]
# //*[@id="idSIButton9"]
driver.find_element_by_xpath('//*[@id="signIn"]').click()
time.sleep(2)
passwordField = driver.find_element_by_id("i0118")
passwordField.clear()
passwordField.send_keys(password)
# //*[@id="CredentialsInputPane"]/div[2]/div/div/div[5]/div/div/div[2]
driver.find_element_by_xpath('//*[@id="CredentialsInputPane"]/div[2]/div/div/div[5]/div/div/div[2]').click()
time.sleep(2)
print("Signed In!")
time.sleep(12)

driver.find_element_by_xpath('//*[@id="menuItem-contacts"]/span[1]/span').click()
print("Contacts Loaded!")
time.sleep(2)

def check_element():
	try:
	    element=driver.find_element_by_xpath('//*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[2]/div/li[7]')
	    return True
	    print("element found")
	except NoSuchElementException:
	    print("No element found")
	    return False

if check_element == True:
	number = 1
	count = driver.find_element_by_xpath('//*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[2]')
	len(count)
	driver.find_element_by_xpath('//*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[2]/div/li[{}]'.format(number)).click()
	print("Single Contact Loaded!")
	time.sleep(4)
else:
	print('bye')


# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul
# //*[@id="swxContent1"]/swx-navigation/div/div[1]/div/div[2]/div[1]/div/ul/div[2]/div/li[2]
# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[21]/div/li[3]

# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[2]/div/li[2]

# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[2]/div/li[1]
# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[2]/div/li[2]
# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[2]/div/li[3]
# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[2]/div/li[4]
# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[2]/div/li[5]

# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[3]/div/li[2]
# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[3]/div/li[1]
# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[3]/div/li[2]
# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[3]/div/li[3]

# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[4]/div/li[1]

# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[21]/div/li[2]


# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[21]/div/li[3]


# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[14]/div/li[3]


# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[20]/div/li[3]

# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[22]/div/li[1]


# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[23]/div/li

# driver.switch_to.frame("textarea_iframe")
# InputBox = driver.find_element_by_xpath('//*[@id="chatInputContainer"]')
InputBox = driver.switch_to_active_element()
InputBox.clear()
print("Message data worked!")
InputBox.send_keys("Hello!")
print("Message Written!")
# InputBox.send_keys(Keys.ENTER)
# driver.find_element_by_xpath('//*[@id="swxContent1"]/swx-navigation/div/div/div/label/div/div/div[2]/div[2]/div/swx-button/button').click()
print("Message Sent!")
driver.back()


# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[2]/p
# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[3]
# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[3]/div
# //*[@id="swxContent1"]/swx-navigation/div/div/div/div[2]/div[1]/div/ul/div[3]/div/li[1]
# def signOut():
#   print("Signing out...")
#   if not driver.find_element_by_class_name("signOut").is_displayed():
#     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME,'summary'))).click()
#   WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME,'signOut'))).click()
#   print("Signed Out!")

# def quit():
#   print("Quitting...")
#   driver.quit()

# def recents():
#   return driver.find_elements_by_tag_name("swx-recent-item")

# def main(args):
#   try:
#     launch()
#     signIn(args.username, args.password)
#     signOut()
#   except:
#     print("Something went wrong")
#   finally:
#     quit()

# def sendMessageToSelected(message):
#   element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.TAG_NAME,'swx-textarea')))
#   element = element.find_element_by_tag_name("textarea")
#   element.click()
#   element.clear()
#   element.send_keys(message)
#   element.send_keys(Keys.ENTER)

# def sendMessage(tileName, message):
#   recent(tileName).click()
#   sendMessageToSelected(message)

# def getTileName(element):
#   return element.find_element_by_class_name("tileName").text

# def recent(tileName):
#   for recentTile in recents():
#     if getTileName(recentTile) == tileName:
#       return recentTile

# def ss(path="ss.png"):
#   driver.save_screenshot(path)

# if __name__ == "__main__":
#   print("Starting up...")
#   parser = argparse.ArgumentParser(description='pySkypeBot: Python Skype Bot')
#   parser.add_argument('-u', '--username', help='Skype User Name')
#   parser.add_argument('-p', '--password', help='Skype Password')
#   main(parser.parse_args())
