import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestEx16(unittest.TestCase):



    def test_ex_1(self):
        try:
            link = 'http://suninjuly.github.io/registration1.html'

            driver = webdriver.Chrome()
            driver.get(link)


            first_name = driver.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
            first_name.send_keys('Ivan')

            last_name = driver.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
            last_name.send_keys('Ivanov')

            email = driver.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
            email.send_keys('Ivanov@gmail.com')

            submit_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
            submit_btn.click()

            welcome_text_bilboard = driver.find_element(By.XPATH, '//div[@class="container"]')

            self.assertEqual((welcome_text_bilboard.text), 'Congratulations! You have successfully registered!', 'Test is good')
        finally:
            time.sleep(1)



    def test_ex_2(self):
        try:
            link = 'http://suninjuly.github.io/registration2.html'

            driver = webdriver.Chrome()
            driver.get(link)

            first_name = driver.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
            first_name.send_keys('Ivan')

            last_name = driver.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
            last_name.send_keys('Ivanov')

            email = driver.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
            email.send_keys('Ivanov@gmail.com')

            submit_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
            submit_btn.click()

            welcome_text_bilboard = driver.find_element(By.XPATH, '//div[@class="container"]')

            self.assertEqual((welcome_text_bilboard.text), 'Congratulations! You have successfully registered!', 'Test is good')
        finally:
            time.sleep(1)
            driver.quit()


if __name__ == "__main__":
    unittest.main()