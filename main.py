from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import json
import time


class Registrant():
    def __init__(self, driver_kind='Firefox', silent=True, student_ID=None, password=None) -> None:
        '''
        # Parameters
        student_ID & password : you can also use Registrant().set_ID_password() to set

        driver_kind : {'Firefox', 'Chrome'}, default='Firefox

        silent : bool, default=True
            Not to open the browser window
        '''
        self.student_ID = student_ID
        self.password = password
        self.silent = silent
        if driver_kind == 'Firefox':
            self.options = webdriver.FirefoxOptions()
            self.initOptions()
            self.driver = webdriver.Firefox(options=self.options)
        elif driver_kind == 'Chrome':
            self.options = webdriver.ChromeOptions()
            self.initOptions()
            self.driver = webdriver.Chrome(options=self.options)
        else:
            raise ValueError

    def initOptions(self):
        '''
        浏览器启动参数
        '''
        self.options.headless = self.silent
        self.options.add_argument('--disable-images')
        # self.options.add_experimental_option('detach', True)
        # self.options.add_experimental_option('useAutomationExtension', False)
        # self.options.add_experimental_option(
        #     'excludeSwitches', ['enable-automation'])

    def set_ID_password(self, student_ID=None, password=None):
        self.student_ID = student_ID
        self.password = password

    def register(self, url='https://m.ruc.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fm.ruc.edu.cn%2Fsite%2FapplicationSquare%2Findex%3Fsid%3D2'):
        if not (self.student_ID and self.password):
            raise ValueError
        self.driver.get(url)
        # account -> password -> login
        self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div[2]/div[1]/input').send_keys(self.student_ID)
        self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div[2]/div[2]/input').send_keys(self.password)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]').click()

        # Daily report
        WebDriverWait(driver=self.driver, timeout=10,
                      poll_frequency=0.5).until(lambda driver: driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/section/div/div[3]/div/ul/li/span'))
        self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div[1]/div/section/div/div[3]/div/ul/li/span').click()

        # Location -> Submit
        WebDriverWait(driver=self.driver, timeout=10,
                      poll_frequency=0.5).until(lambda driver: driver.find_element(By.XPATH, '/html/body/div[1]/div/div/section/div[4]/ul/li[8]/div/input'))
        self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div/section/div[4]/ul/li[8]/div/input').click()
        time.sleep(1)
        self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div/section/div[5]/div/a').click()
        time.sleep(1)
        try:
            self.driver.find_element(
                By.XPATH, '/html/body/div[4]/div/div[2]/div[2]').click()
        except NoSuchElementException:
            print('今日已填报')
        else:
            print('成功填报')
        time.sleep(5)
        quit()

    def debug(self):
        print(self.student_ID)


if __name__ == '__main__':
    with open('./setting.json', 'r', encoding='utf8') as fp:
        student_info = json.load(fp)
    reg = Registrant(silent=True)
    reg.set_ID_password(student_info['student_ID'], student_info['password'])
    reg.register()