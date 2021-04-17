from django.test import TestCase
from .models import *

class testArticle(TestCase):
    def setUp(self):
        self.bmn = Article(title='Test a', article_link='http.google.com' )

    def test_instance(self):
        self.assertTrue(isinstance(self.bmn, Article))

    def test_save(self):
        self.bmn.save_base()
        article = Article.objects.all()
      

        self.assertTrue(len(article) > 0)

class Profile(TestCase):
    def setUp(self):
        self.sam = TeacherProfile(name='sam', phone_number='234467', email='fjg@fif.com', my_posts='test b')
        