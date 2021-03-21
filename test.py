from headless_mode import healdess
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

# driver = webdriver.Chrome()
driver.get('https://univer.kaznu.kz/user/login?ReturnUrl=%2f')

sleep(10)

login = driver.find_element_by_xpath('//*[@id="id_login"]')

password = driver.find_element_by_xpath('//*[@id="id_pass"]')


login.send_keys("Логин")


password.send_keys("Пароль")

sleep(10)

button_click = driver.find_element_by_xpath('//*[@id="login_form"]/input[3]')

button_click.send_keys(Keys.RETURN)

sleep(10)
magistrant = driver.find_element_by_xpath('//*[@id="l3"]/td/table/tbody/tr/td[2]/a[2]')

magistrant.send_keys(Keys.RETURN)

sleep(10)
schedule = driver.find_element_by_xpath('//*[@id="tools"]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/ul/li[2]/a[1]')

schedule.send_keys(Keys.RETURN)

sleep(10)


for horizontally in range(2, 8):
	for vertical in range(2, 10):


		week = driver.find_element_by_xpath('//*[@id="files_list"]/td[2]/div/table/tbody/tr[1]/th[' + str(horizontally) + ']')

		time = driver.find_element_by_xpath('//*[@id="files_list"]/td[2]/div/table/tbody/tr[' + str(vertical) + ']/td[1]')
		#//*[@id="files_list"]/td[2]/div/table/tbody/tr[3]/td[1]

		timetable = driver.find_element_by_xpath("//*[@id='files_list']/td[2]/div/table/tbody/tr[" + str(vertical) + "]/td[" + str(horizontally) + "]")

		print(week.text + "  " + time.text + " " + timetable.text )
		print("______________________________________")



		sleep(5)

driver.close()

