from selenium import webdriver
from time import sleep

your_mail_id = "YOUR MAIL ID"
your_password = 'ENTER YOUR PASSWORD'
# Specify your driver(eg. Chrome or Firefox) path below
path = "YOUR DRIVER LOCATION"
driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()
# Speed_test screen
print('---------- Getting your internet speed details ----------')
driver.get("https://www.speedtest.net/")
sleep(5)
go = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
print('Checking download speed /--')
sleep(40)
download_speed_result = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                     '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
print(f"Here's your download speed report {download_speed_result}mpbs.")
print('Checking upload speed /--')
sleep(40)
upload_speed_test = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                 '3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
print(f"Here's your upload speed report {upload_speed_test}mpbs")
print("####  Screen will change  ####")
download = float(download_speed_result)
upload = float(upload_speed_test)
# Twitter screen
driver.get('https://twitter.com/')
print("---------- Changed into twitter screen ----------")
second_screen = driver.window_handles[0]
driver.switch_to.window(second_screen)
sleep(5)
login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div').click()
print('Clicked login button')
email = driver.find_element_by_name('session[username_or_email]')
email.send_keys(your_mail_id)
password = driver.find_element_by_name('session[password]')
password.send_keys(your_password)
print('credentials are filled')
credential_login = driver.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
credential_login.click()
print('Successfully login.')
sleep(15)
print('Checking condition for write a post ----------/')
def message(content):
    post = driver.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div['
        '2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div['
        '1]/div/div/div/div[2]/div/div/div/div')
    post.send_keys(content)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div['
        '2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div['
        '3]/div/span/span').click()

if download and upload > 10:
    # PASS THE VALUE WHAT YOU WANT TO POST ON YOUR TWITTER
    message(f'My Download internet speed is {download}mpbs and Upload internet speed is {upload}mpbs.\n Good internet speed :)')
else:
    # PASS THE VALUE WHAT YOU WANT TO POST ON YOUR TWITTER
    message(f'My Download internet speed is {download}mpbs and Upload internet speed is {upload}mpbs.\n Bad internet speed :)')
print("Successfully Tweet posted....")