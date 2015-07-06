from django.test import TestCase

from app.blog.forms import PostForm
from app.blog.tests import LONG_BLOG_POST

class PostFormTests(TestCase):
    
    def test_new_small_post_form_should_be_valid(self):
        expectedContent = "some small content"
        expectedTitle = 'blog title'
        form_data =  {'title': expectedTitle, 'content': expectedContent}
        
        form = PostForm(data=form_data)
        
        self.assertEqual(form.is_valid(), True)
        self.assertEqual(expectedContent, form.data['content'])
        self.assertEqual(expectedTitle, form.data['title'])
    
    def test_new_large_post_form_should_be_valid(self):
        expectedContent = LONG_BLOG_POST
        expectedTitle = 'blog title'
        form_data =  {'title': 'blog title', 'content': LONG_BLOG_POST}
        
        form = PostForm(data=form_data)
        
        self.assertEqual(form.is_valid(), True)
        self.assertEqual(expectedContent, form.data['content'])
        self.assertEqual(expectedTitle, form.data['title'])
        
    def test_new_post_no_title_should_contain_error(self):
        form_data =  {'content': LONG_BLOG_POST}
        
        form = PostForm(data=form_data)
        
        self.assertEqual(form.is_valid(), False)
        self.assertEqual(form.errors, { 'title' : [u'This field is required.'] })
        
    def test_new_post_no_content_should_contain_error(self):
        form_data =  {'title': 'my title'}
        
        form = PostForm(data=form_data)
        
        self.assertEqual(form.is_valid(), False)
        self.assertEqual(form.errors, { 'content' : [u'This field is required.'] })
        