import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class BasicInstallTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_install(self):  
        # В браузере открылся сайт (по адресу: 'http://127.0.0.1:8000')
        # В заголовке сайта прочитали "Сайт Алексея Куличевского"

        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Сайт Алексея Куличевского', self.browser.title)

    def test_home_page_header(self):
        # В шапке сайта написно "Алексей Куличевский"
        self.browser.get('http://127.0.0.1:8000')
        header = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertIn('Алексей Куличевский', header.text)

if __name__ == '__main__':  
    unittest.main()

# self.fail('Finish test!')