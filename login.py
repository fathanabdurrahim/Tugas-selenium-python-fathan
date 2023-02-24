import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogindanregister(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_Register(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(1)
        driver.find_element(By.ID,"signUp").click()# buka singup
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("Dom") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("Dom@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("kuy123") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"swal2-html-container").text
        self.assertIn('created user!', response_data)

    def test_b_Login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(1)

      

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
