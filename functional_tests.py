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
        # У каждой статьи есть заголовок и один абзац с текстом
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        article_summary = self.browser.find_element(By.CLASS_NAME, 'article-summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)

    def test_home_page_article_title_link_leads_to_article_page(self):
        # Вася кликнул по заголовку и у него открылась страница с полным текстом
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        article_title_text = article_title.text

        # Находим ссылку в заголовке статьи
        article_link = article_title.find_element(By.TAG_NAME, 'a')

        # Переходим по ссылке
        self.browser.get(article_link.get_attribute('href'))

        # Ожидаем, что на открывшейся странице есть нужная статья
        article_page_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        self.assertEqual(article_title_text, article_page_title.text)


if __name__ == '__main__':  
    unittest.main()

# self.fail('Finish test!')


# Вася попытался открыть несуществующую статью и ему открыласькрасивая страничка "Страница не найдена"

# Прочитал статью, кликнул по тексту "Алексей Кулический" и попал на главную страницу

# Некоторые статьи есть в админке, но они опубликованы

# Статьи открываются с красивым коротким адресом