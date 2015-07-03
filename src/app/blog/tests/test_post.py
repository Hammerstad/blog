from django.contrib.auth.models import User
from django.test import TestCase

from app.blog.models import Post
from app.blog.tests import LONG_BLOG_POST

class PostTestCase(TestCase):
    
    def setUp(self):
        user = User.objects.create_user('testuser', 'testuser@test.com', 'testpassword')
        Post.objects.create(creator=user, title="Small post", content="some small content")
        Post.objects.create(creator=user, title="Long post", content=LONG_BLOG_POST)

    def test_small_post_has_same_content_and_summary(self):
        small_post = Post.objects.get(title="Small post")
        expected = "some small content"
        self.assertEqual(expected, small_post.content)
        self.assertEqual(expected, small_post.summary)
    
    def test_long_post_has_summary_created_from_content(self):
        small_post = Post.objects.get(title="Long post")
        expected_summary = LONG_BLOG_POST[:300]
        self.assertEqual(expected_summary, small_post.summary)