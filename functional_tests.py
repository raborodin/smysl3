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


    def test_home_page_blog(self):
        # Под шапкой должен быть расположен блок со статьями
        self.browser.get('http://127.0.0.1:8000')
        article_list = self.browser.find_element(By.CLASS_NAME, 'article-list')
        self.assertTrue(article_list)

    def test_home_page_blog_articles_look_correct(self):
        # У каждоый статьи есть заголовок и один абзац с текстом
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        article_summary = self.browser.find_element(By.CLASS_NAME, 'article-summary')
        self.assertIn(article_title)
        self.assertIn(article_summary)


if __name__ == '__main__':  
    unittest.main()

# self.fail('Finish test!')