from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep,ctime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

DMART='https://dmart.in/'
opts = Options()
browser = Firefox(options=opts)
browser.get(DMART)
action = ActionChains(browser)
print("Dmart Home Page Opened......")
# /html/body/div[19]/div[1]
init_addr = "<Insert Your Pincode with Local Area>"
pin_code_form = browser.find_element_by_id('pinNumberModal')
pin_code_form.send_keys(init_addr)
sleep(2)
pin_code_form.send_keys(Keys.RETURN)
proceed_btn = browser.find_element_by_id('btnPinSubmit')
proceed_btn.click()
browser.find_element(By.XPATH,"/html/body/div[1]/header[1]/div[3]/div/div[3]/section/div/div[3]/div/div[2]/ul/li/a[1]").click()
mob_no = browser.find_element(By.XPATH,"/html/body/div[1]/header[1]/div[3]/div/div[3]/section/div/div[3]/div/div[2]/ul/li/div[1]/div/div/form/div[3]/div/input")
mob_no.send_keys("<Enter Mobile Number>")
pwd = browser.find_element(By.XPATH,"/html/body/div[1]/header[1]/div[3]/div/div[3]/section/div/div[3]/div/div[2]/ul/li/div[1]/div/div/form/div[4]/div[1]/div/input")
pwd.send_keys("<Enter Password>")
browser.find_element(By.XPATH,"/html/body/div[1]/header[1]/div[3]/div/div[3]/section/div/div[3]/div/div[2]/ul/li/div[1]/div/div/form/div[7]/button[1]").click()
print("Now Logged in....")
sleep(2)
isAvail=False
count=0
while(isAvail==False):
	count=count+1
	browser.get("https://www.google.com/")
	browser.get(DMART)
	sleep(1)
	browser.get("https://dmart.in/delivery?currentAction=Delivery")
	sleep(4)
	browser.find_element(By.XPATH,'//*[@id="29511"]').click()
	sleep(2)
	browser.find_element(By.XPATH,"/html/body/div[7]/div/div[2]/div[2]/div/div/div[2]/a").click()
	sleep(2)
	row_days = browser.find_elements_by_css_selector("div.delivery-selection-row")

	for row in row_days:
		for col in row.find_elements_by_tag_name('span'):
			# print(col.get_attribute('class'))
			if(col.get_attribute('class')!='delivery-slot--not-selectable'):
				isAvail=True
	sleep(4)

print("Slot Made Available....:")
print("Number of times to execute:",count)

