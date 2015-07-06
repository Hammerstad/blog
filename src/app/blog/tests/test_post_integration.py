from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import Client, TestCase

class PostTestCase(TestCase):
	
	def setUp(self):
		user = User.objects.create_user('testuser', 'testuser@test.com', 'testpassword')
		user.save()
	
	def test_new_post_with_http_get_returns_new_form(self):
		x = self.client.login(username='testuser', password='testpassword')
		response = self.client.post(reverse("new_post"), {'title': 'blog title', 'content': 'lorem ipsum'})
		self.assertEqual(response.status_code, 200)